{{- define "archi-v2.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "archi-v2.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "archi-v2.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end }}

{{- define "archi-v2.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "archi-v2.labels" -}}
helm.sh/chart: {{ include "archi-v2.chart" . }}
app.kubernetes.io/name: {{ include "archi-v2.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: archi-crab-bench
{{- end }}

{{- define "archi-v2.selectorLabels" -}}
app.kubernetes.io/name: {{ include "archi-v2.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/* image reference: repository@digest when a digest is pinned, else repository:tag */}}
{{- define "archi-v2.image" -}}
{{- if .digest -}}{{ printf "%s@%s" .repository .digest }}{{- else -}}{{ printf "%s:%s" .repository (default "latest" .tag) }}{{- end -}}
{{- end }}

{{/* Postgres env the archi services read (PostgresServiceFactory.from_env + the config's host) */}}
{{- define "archi-v2.pgEnv" -}}
- name: PGHOST
  value: {{ include "archi-v2.fullname" . }}-postgres
- name: PGPORT
  value: {{ .Values.postgres.port | quote }}
- name: PGDATABASE
  value: {{ .Values.postgres.database | quote }}
- name: PGUSER
  value: {{ .Values.postgres.user | quote }}
- name: PG_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: PG_PASSWORD
{{- end }}

{{- define "archi-v2.secretEnv" -}}
- name: {{ .key }}
  valueFrom:
    secretKeyRef:
      name: {{ .secret }}
      key: {{ .key }}
      optional: {{ .optional | default false }}
{{- end }}
