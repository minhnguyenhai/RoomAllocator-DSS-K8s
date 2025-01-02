apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  type: {{ .Values.service.frontend.type }}
  ports:
    - port: 80
      targetPort: 80
  selector:
    app: frontend
---
apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  type: {{ .Values.service.backend.type }}
  ports:
    - port: 5000
      targetPort: 5000
  selector:
    app: backend
