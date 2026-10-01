# Curated CMS TWiki topics (source `twiki` in ../../source_registry.yaml)

One subdirectory per TWiki web, raw topic files exactly as TWiki stores them
(`%META:TOPICINFO` / `%META:TOPICPARENT` lines included):

    CMS/<Topic>.txt          <- scripts/twiki-curate.py --src /eos/.../twiki/CMS/topics --out data/twiki/CMS
    CMSPublic/<Topic>.txt    <- same, from the CMSPublic snapshot if one exists

Never put a `.txt` at this top level: the reader takes the first path part as
the web name. Files starting with `.` and non-`.txt` files (this README, the
`.curated` marker) are ignored by the reader.

CMS-web pages are CMS-internal. This repository must stay private, and the MCP
serves them to `cms-members` only (Cedar policy in CMSKubernetes mcp-gateway).
Refresh: re-run the curate script with the same flags, then
`git add -A deployments/archi-crab/data/twiki && git diff --cached --stat`
(new pages are untracked until added), review, commit.
