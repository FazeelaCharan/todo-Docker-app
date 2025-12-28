# Cluster Setup (Kubernetes)

## Environment
- OS: Windows 11
- Kubernetes: Docker Desktop built-in Kubernetes
- kubectl: Installed via Docker Desktop

## Steps to Enable Kubernetes
1. Open Docker Desktop
2. Go to Settings → Kubernetes
3. Enable Kubernetes
4. Wait for cluster to start

## Verification Commands

```bash
kubectl cluster-info
kubectl get nodes
```