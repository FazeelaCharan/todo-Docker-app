# Kubernetes Deployment – Flask To-Do App

This folder contains Kubernetes manifests to deploy the Dockerized Flask application.

## Files Included

- deployment.yaml – Deployment with 3 replicas
- service.yaml – NodePort service to expose the app
- configmap.yaml – Non-sensitive configuration
- secret.yaml – Dummy secret for demonstration

## Deploy Application

From the project root, run:

```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get svc
kubectl get deploy
```

## Access the Application

http://localhost:30007

## Scaling the Application

```bash
kubectl scale deployment flask-demo-app --replicas=5
kubectl get pods
```

## Rolling update

After changing theDocker image tag

```bash
kubectl apply -f k8s/deployment.yaml
kubectl rollout status deployment flask-demo-app
kubectl rollout history deployment flask-demo-app
```
