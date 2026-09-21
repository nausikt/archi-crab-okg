{{- define "okg.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "okg.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "okg.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end }}

{{- define "okg.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "okg.labels" -}}
helm.sh/chart: {{ include "okg.chart" . }}
app.kubernetes.io/name: {{ include "okg.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "okg.selectorLabels" -}}
app.kubernetes.io/name: {{ include "okg.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "okg.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
{{- default (include "okg.fullname" .) .Values.serviceAccount.name -}}
{{- else -}}
{{- required "serviceAccount.name is required when serviceAccount.create=false" .Values.serviceAccount.name -}}
{{- end -}}
{{- end }}

{{- define "okg.runtimeImage" -}}
{{- if .Values.images.okg.digest -}}
{{- printf "%s@%s" .Values.images.okg.repository .Values.images.okg.digest -}}
{{- else -}}
{{- printf "%s:%s" .Values.images.okg.repository (required "images.okg.tag is required when digest is empty" .Values.images.okg.tag) -}}
{{- end -}}
{{- end }}

{{- define "okg.postgresImage" -}}
{{- if .Values.postgresql.image.digest -}}
{{- printf "%s@%s" .Values.postgresql.image.repository .Values.postgresql.image.digest -}}
{{- else -}}
{{- printf "%s:%s" .Values.postgresql.image.repository (required "postgresql.image.tag is required when digest is empty" .Values.postgresql.image.tag) -}}
{{- end -}}
{{- end }}

{{- define "okg.commonEnv" -}}
{{- /*
  The deployment manifest is baked into the image (`COPY . .`), so the pod reads
  the SAME deployment.yaml as the host checkout. A static runtime.supervisor in
  that file cannot be truthful for both targets: okg-workspace runs as a host
  launchd worker AND as this container. This declares the adapter for THIS
  instantiation. It is a declaration, not inference -- the chart's values are the
  deployment configuration for this target -- which is why the code is forbidden
  from sniffing /.dockerenv or platform.system() instead.
*/ -}}
- name: OKG_RUNTIME_SUPERVISOR
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: runtime-supervisor
- name: OKG_DEPLOYMENT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: deployment
- name: OKG_REPO_ROOT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: repo-root
{{- if .Values.repositorySync.enabled }}
- name: OKG_DEPLOYMENTS_DIR
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: deployments-dir
{{- end }}
{{- /* archi-crab delta 5: archi connectors resolve relative data/ paths against
       ARCHI_DATA_ROOT (else cwd). Same value as OKG_ENVIRONMENT_DATA_ROOT by
       design — both read the one ConfigMap key so they cannot diverge. */}}
- name: ARCHI_DATA_ROOT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: environment-data-root
- name: OKG_ENVIRONMENT_DATA_ROOT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: environment-data-root
- name: OKG_RUNTIME_ENVIRONMENT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: runtime-environment
{{- end }}

{{- define "okg.runtimeSubjectEnv" -}}
- name: OKG_NOMOS_SUBJECT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: runtime-nomos-subject
{{- end }}

{{- define "okg.mcpSubjectEnv" -}}
- name: OKG_NOMOS_SUBJECT
  valueFrom:
    configMapKeyRef:
      name: {{ include "okg.fullname" . }}
      key: mcp-nomos-subject
{{- end }}

{{- define "okg.extraSecretEnvFor" -}}
{{- $root := index . 0 -}}
{{- $target := index . 1 -}}
{{- range $entry := $root.Values.secrets.extraEnv }}
{{- if has $target $entry.targets }}
- name: {{ $entry.name }}
  valueFrom:
    secretKeyRef:
      name: {{ $root.Values.secrets.existingSecret }}
      key: {{ $entry.key }}
{{- end }}
{{- end }}
{{- end }}

{{- define "okg.writerDsnEnv" -}}
- name: OKG_DSN
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: {{ .Values.secrets.externalDsnKey }}
{{- if ne .Values.okg.deploymentDsnEnv "OKG_DSN" }}
- name: {{ .Values.okg.deploymentDsnEnv }}
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: {{ .Values.secrets.externalDsnKey }}
{{- end }}
{{- end }}

{{- define "okg.readerDsnEnv" -}}
- name: OKG_DSN
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: {{ .Values.secrets.mcpDsnKey }}
- name: OKG_MCP_RO_DSN
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: {{ .Values.secrets.mcpDsnKey }}
{{- if ne .Values.okg.deploymentDsnEnv "OKG_DSN" }}
- name: {{ .Values.okg.deploymentDsnEnv }}
  valueFrom:
    secretKeyRef:
      name: {{ .Values.secrets.existingSecret }}
      key: {{ .Values.secrets.mcpDsnKey }}
{{- end }}
{{- end }}

{{- define "okg.containerSecurityContext" -}}
allowPrivilegeEscalation: false
capabilities:
  drop: ["ALL"]
readOnlyRootFilesystem: true
runAsNonRoot: true
runAsUser: 10001
runAsGroup: 10001
seccompProfile:
  type: RuntimeDefault
{{- end }}
