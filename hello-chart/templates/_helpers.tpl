{{- define "app" -}}
{{ .Release.Name }}{{- print "-app"}}
{{- end -}}

{{- define "web" -}}
{{ .Release.Name }}{{- print "-web"}}
{{- end -}}
