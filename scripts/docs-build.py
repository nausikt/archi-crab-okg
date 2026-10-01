#!/usr/bin/env python3
"""docs-build — turn a folder of pages (Markdown, HTML, PDF) into the one
records.json a `docs-files` source reads (archi's DocumentationSource).

Run it where the files are (laptop, lxplus), commit the output, and
repositorySync delivers it to the pod. Needs python3 >= 3.9; PDFs need
`pip install pypdf` or poppler's `pdftotext` on PATH.

  python3 scripts/docs-build.py \\
      --src ~/sources/10_sanitized_twikis \\
      --out deployments/archi-crab/data/docs/twiki-sanitized \\
      --report /tmp/twiki-sanitized.csv --dry-run      # review, then drop --dry-run

Each file becomes one page whose identity is its URL (the graph keys the page
by it and every answer cites it). The URL comes from the file name:

  <Web>_<Topic>.<ext>  ->  https://twiki.cern.ch/twiki/bin/view/<Web>/<Topic>
  CMSPublic_CRAB3FAQ.md -> .../bin/view/CMSPublic/CRAB3FAQ

(--url-template changes the pattern; --urls FILE maps odd names explicitly, one
`<file name><TAB><url>` per line.) When one page exists in several formats, one
is kept: md, then html, then pdf. A file is refused (and listed in the report
with the reason) when it has no URL, is empty or under --min-chars, or looks
like a CERN login page. E-mail addresses are replaced by <email> unless
--keep-emails. The output is sorted and one record per line, so a rebuild's
`git diff` shows exactly which pages changed.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

FORMATS = {".md": "md", ".markdown": "md", ".html": "html", ".htm": "html", ".pdf": "pdf", ".txt": "md"}
PRECEDENCE = {"md": 0, "html": 1, "pdf": 2}
LOGIN_RE = re.compile(r"auth\.cern\.ch/auth/realms|Sign in with your CERN|CERN Single Sign-On|login\.cern\.ch", re.I)
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
NAME_RE = re.compile(r"^(?P<web>[A-Z][A-Za-z0-9]*)_(?P<topic>[A-Za-z0-9][A-Za-z0-9_]*)$")
DEFAULT_TEMPLATE = "https://twiki.cern.ch/twiki/bin/view/{web}/{topic}"


# ---------------------------------------------------------------- readers ----

def read_markdown(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    title = ""
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if fm:
        m = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", fm.group(1), re.M)
        title = m.group(1) if m else ""
        text = text[fm.end():]
    if not title:
        m = re.search(r"^#{1,2}\s+(.+?)\s*#*\s*$", text, re.M)
        title = m.group(1) if m else ""
    return title, text, ""


class _HTMLText(HTMLParser):
    """HTML -> Markdown-ish text: headings as #, list items as -, <pre> kept
    verbatim in fences, table cells joined with |. Skips script/style/head and,
    when given a marker, everything outside that one <div> (on a rendered TWiki
    page: the topic body, without the breadcrumb, edit bar and revision line).

    Only <div> nesting is counted to find the end of the marked div, so an
    unclosed <p>/<li> or a stray </span> -- common in real pages -- cannot end
    it early or late."""

    SKIP = {"script", "style", "noscript", "head", "nav", "footer", "form", "button", "select"}
    BLOCK = {"p", "div", "section", "article", "br", "tr", "table", "ul", "ol", "dl", "dt", "dd", "blockquote", "hr"}

    def __init__(self, marker=None):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.pre, self.title, self.in_title = [], 0, 0, "", False
        self.marker = marker                       # ("class"|"id", value) or None
        self.state = "before" if marker else "in"  # before -> in -> after
        self.divs = 0

    def _is_marker(self, tag, a):
        if tag != "div" or not self.marker:
            return False
        what, value = self.marker
        return a.get("id") == value if what == "id" else value in (a.get("class") or "").split()

    def _on(self):
        return self.skip == 0 and self.state == "in"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if self.state == "before" and self._is_marker(tag, a):
            self.state, self.divs = "in", 1
            return
        if self.state == "in" and self.marker and tag == "div":
            self.divs += 1
        if tag in self.SKIP:
            self.skip += 1
        if not self._on():
            return
        if re.fullmatch(r"h[1-6]", tag):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "pre":
            self.pre += 1
            self.out.append("\n```\n")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        on = self._on()
        if on and tag == "pre":
            self.pre = max(0, self.pre - 1)
            self.out.append("\n```\n")
        elif on and (re.fullmatch(r"h[1-6]", tag) or tag in self.BLOCK):
            self.out.append("\n")
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        if self.state == "in" and self.marker and tag == "div":
            self.divs -= 1
            if self.divs == 0:
                self.state = "after"

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self._on():
            self.out.append(data if self.pre else re.sub(r"\s+", " ", data))


def _html_marker(raw):
    """The topic body on a rendered TWiki page: patternTopic (the topic text
    alone) before patternMainContents (which also holds breadcrumb and edit bar)."""
    if re.search(r'<div[^>]*class="[^"]*\bpatternTopic\b', raw):
        return ("class", "patternTopic")
    if re.search(r'<div[^>]*id="patternMainContents"', raw):
        return ("id", "patternMainContents")
    return None


def _parse_html(raw, marker):
    p = _HTMLText(marker)
    p.feed(raw)
    p.close()
    return p, "".join(p.out)


def read_html(path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    marker = _html_marker(raw)
    p, text = _parse_html(raw, marker)
    note = ""
    if marker and len(text.strip()) < 200:
        p, text = _parse_html(raw, None)
        note = "topic body not found (%s=%s); whole page kept" % marker
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = (m.group(1) if m else "") or html.unescape(p.title).strip()
    return title.strip(), text, note


def read_pdf(path):
    try:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # pypdf's cryptography deprecation noise
            from pypdf import PdfReader
    except ImportError:
        PdfReader = None
    if PdfReader is not None:
        reader = PdfReader(str(path))
        text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
        title = str((reader.metadata or {}).get("/Title") or "") if reader.metadata else ""
        import pypdf
        EXTRACTORS.add("pypdf %s" % getattr(pypdf, "__version__", "?"))
        return title, text, ""
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, timeout=120)
        if r.returncode == 0:
            EXTRACTORS.add("pdftotext -layout")
            return "", r.stdout, ""
        raise RuntimeError("pdftotext: %s" % r.stderr.strip()[:200])
    raise RuntimeError("no PDF reader: pip install pypdf (or install poppler-utils)")


READERS = {"md": read_markdown, "html": read_html, "pdf": read_pdf}
EXTRACTORS = set()  # which PDF extractor built this output (recorded in build.json)


def redact_emails(text):
    """Replace e-mail addresses, but not look-alikes that are commands: scp/git
    syntax (git@github.com:org/repo, user@host:path) and login targets
    (user@lxplus.cern.ch)."""
    n = [0]

    def sub(m):
        local, dom = m.group(0).split("@", 1)
        if m.string[m.end():m.end() + 1] == ":" or local == "git" or re.match(
                r"(lxplus|lxtunnel|aiadm|cmslpc|lxbatch|lxslc)[\w-]*\.", dom, re.I):
            return m.group(0)
        n[0] += 1
        return "<email>"

    return EMAIL_RE.sub(sub, text), n[0]


def tidy(text):
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# ------------------------------------------------------------------ build ----

def load_url_map(path):
    out = {}
    if not path:
        return out
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2 or not parts[1].startswith(("http://", "https://")):
            sys.exit("%s:%d: expected <file name><TAB><url>" % (path, n))
        out[parts[0].strip()] = parts[1].strip()
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--src", required=True, help="folder of .md/.html/.pdf files (not recursive)")
    ap.add_argument("--out", required=True, help="output dir, e.g. deployments/archi-crab/data/docs/twiki-sanitized")
    ap.add_argument("--url-template", default=DEFAULT_TEMPLATE, help="default: %(default)s")
    ap.add_argument("--urls", help="TSV of <file name><TAB><url> for names the template cannot map")
    ap.add_argument("--site-name", default="twiki.cern.ch")
    ap.add_argument("--min-chars", type=int, default=200)
    ap.add_argument("--webs", help="keep only these TWiki webs, e.g. CMSPublic (comma-separated). A source declared "
                    "`sensitivity: public` must hold public webs only; build the rest as a separate source")
    ap.add_argument("--keep-emails", action="store_true")
    ap.add_argument("--twiki-dir", help="curated raw TWiki dir to report overlaps with (default: <out>/../../twiki)")
    ap.add_argument("--report", help="CSV: file,web,topic,url,format,chars,status,note")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any file is refused")
    a = ap.parse_args(argv)

    src, out = Path(a.src).expanduser(), Path(a.out)
    if not src.is_dir():
        sys.exit("--src %s is not a directory" % src)
    url_map = load_url_map(a.urls)
    webs = {w.strip() for w in a.webs.split(",") if w.strip()} if a.webs else None
    rows, pages = [], {}
    entries = sorted(p for p in src.iterdir() if not p.name.startswith("."))
    for d in (p for p in entries if p.is_dir()):
        rows.append({"file": d.name + "/", "web": "", "topic": "", "url": "", "format": "dir", "chars": 0,
                     "status": "subdir_skipped", "note": "not recursive: flatten it or build it as its own source"})
    files = [p for p in entries if p.is_file()]
    for path in files:
        fmt = FORMATS.get(path.suffix.lower())
        row = {"file": path.name, "web": "", "topic": "", "url": "", "format": fmt or path.suffix, "chars": 0, "status": "", "note": ""}
        rows.append(row)
        if not fmt:
            row["status"] = "unsupported"
            continue
        m = NAME_RE.match(path.stem)
        if m:
            row["web"], row["topic"] = m.group("web"), m.group("topic")
        if webs is not None and row["web"] not in webs:
            row["status"], row["note"] = "web_filtered", "web %r not in --webs" % (row["web"] or "?")
            continue
        url = url_map.get(path.name) or (a.url_template.format(web=row["web"], topic=row["topic"]) if m else "")
        if not url:
            row["status"], row["note"] = "unmapped", "name is not <Web>_<Topic>; add it to --urls"
            continue
        row["url"] = url
        try:
            title, body, note = READERS[fmt](path)
        except Exception as exc:  # noqa: BLE001 -- report and go on
            row["status"], row["note"] = "unreadable", str(exc)[:200]
            continue
        body = tidy(body)
        notes = [note] if note else []
        if not a.keep_emails:
            body, n = redact_emails(body)
            if n:
                notes.append("%d e-mail(s) redacted" % n)
        row["note"] = "; ".join(notes)
        row["chars"] = len(body)
        if len(body) < 3000 and LOGIN_RE.search(body):
            row["status"] = "login_page"
            continue
        if len(body.strip()) < a.min_chars:
            row["status"] = "too_short"
            continue
        rec = {"url": url, "title": (title or row["topic"] or path.stem).strip(), "site_name": a.site_name,
               "path": "%s/%s" % (row["web"], row["topic"]) if m else path.stem, "body": body}
        prev = pages.get(url)
        if prev and PRECEDENCE[prev[0]] <= PRECEDENCE[fmt]:
            row["status"], row["note"] = "shadowed", "same page kept from %s" % prev[1]["file"]
            continue
        if prev:
            prev[1]["status"], prev[1]["note"] = "shadowed", "same page kept from %s" % path.name
        pages[url] = (fmt, row, rec)
        row["status"] = "kept"

    twiki_dir = Path(a.twiki_dir) if a.twiki_dir else out.parent.parent / "twiki"
    overlap = []
    if twiki_dir.is_dir():
        raw = {"%s/%s" % (p.parent.name, p.stem) for p in twiki_dir.glob("*/*.txt")}
        overlap = sorted(r["web"] + "/" + r["topic"] for r in rows if r["status"] == "kept" and r["web"] + "/" + r["topic"] in raw)

    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("files: %d  %s" % (len(rows), " ".join("%s=%d" % kv for kv in sorted(counts.items()))))
    by_web = {}
    for r in rows:
        if r["status"] == "kept":
            by_web[r["web"] or "(mapped)"] = by_web.get(r["web"] or "(mapped)", 0) + 1
    print("kept by web: %s  -- every web here must be public for a `sensitivity: public` source" % (
        ", ".join("%s=%d" % kv for kv in sorted(by_web.items())) or "none"))
    for r in rows:
        if r["status"] not in ("kept", "shadowed", "web_filtered"):
            print("  %-12s %s  %s" % (r["status"], r["file"], r["note"]))
    if overlap:
        print("also in the curated raw TWiki (%s): %d page(s), e.g. %s -- the same page would be ingested twice "
              "under two ids; keep it in one source" % (twiki_dir, len(overlap), ", ".join(overlap[:5])))
    if a.report:
        with open(a.report, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["file"])
            w.writeheader()
            w.writerows(rows)
        print("report: %s" % a.report)
    records = [rec for _, (_, _, rec) in sorted(pages.items())]
    if not records:
        print("nothing to write: no page was kept", file=sys.stderr)
        return 1
    if a.dry_run:
        print("dry run: %d page(s) would be written to %s/records.json" % (len(records), out))
    else:
        out.mkdir(parents=True, exist_ok=True)
        order = ("url", "title", "path", "site_name", "body")
        text = "[\n" + ",\n".join(json.dumps({k: r[k] for k in order}, ensure_ascii=False) for r in records) + "\n]\n"
        (out / "records.json").write_text(text, encoding="utf-8")
        (out / "build.json").write_text(json.dumps({
            "tool": "scripts/docs-build.py", "source_dir": src.name, "pages": len(records), "files": len(rows),
            "statuses": counts, "url_template": a.url_template, "emails_redacted": not a.keep_emails,
            "pdf_extractor": sorted(EXTRACTORS), "webs": sorted(webs) if webs else "all",
        }, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("wrote %d page(s) to %s/records.json" % (len(records), out))
    refused = sum(v for k, v in counts.items() if k not in ("kept", "shadowed", "subdir_skipped", "web_filtered"))
    return 1 if (a.strict and refused) else 0


if __name__ == "__main__":
    sys.exit(main())
