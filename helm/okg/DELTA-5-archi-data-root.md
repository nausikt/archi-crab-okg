# Chart delta 5 — ARCHI_DATA_ROOT (required by archi connectors)

archi connectors resolve relative cache paths (`data/cmssw-releases/…`, the
installer's default `archi_data_root: data`) against `ARCHI_DATA_ROOT`, or the
process cwd when unset — and a worker pod's cwd is not the deployment dir.
Anchor it to the runtime-data PVC so caches persist (Runbook v0.5.0 F1):

In `templates/_helpers.tpl`, inside `okg.commonEnv` (next to
`OKG_ENVIRONMENT_DATA_ROOT`):

    - name: ARCHI_DATA_ROOT
      value: {{ .Values.okg.environmentDataRoot | quote }}

Do NOT add it to `secrets.extraEnv` (that path is for secret-backed values
and the name is not in the chart's reserved list anyway). Verify after the
first staging sync:

    kubectl -n archi-crab-staging exec sts/<rel>-runtime -c worker -- sh -c 'echo $ARCHI_DATA_ROOT; ls $ARCHI_DATA_ROOT/data'

Delete this file once applied.
