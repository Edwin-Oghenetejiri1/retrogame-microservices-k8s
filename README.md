# 🕹️ RetroGame Microservices

> End-to-end DevOps project | Microservices in 5 languages | Containerized with Docker | Orchestrated with Kubernetes | CI/CD with GitHub Actions | GitOps with ArgoCD

## 📋 Overview

RetroGame Shop is a full-stack e-commerce platform for retro gaming products built as a microservices architecture. This repository demonstrates real-world DevOps practices including containerization, multi-language CI/CD pipelines, container security scanning, and cloud-native deployment on AWS EKS.

## 🎯 Objectives

- **Containerization:** Package each microservice as a Docker container with its own Dockerfile
- **CI/CD Pipelines:** Automate build, test, scan and deploy for each service independently
- **Security Scanning:** Scan Docker images for vulnerabilities using Trivy
- **GitOps:** Use ArgoCD to manage Kubernetes deployments from a separate manifests repo
- **Multi-language:** Demonstrate DevOps practices across 5 different programming languages

## 🏗️ Architecture

```
┌─────────────────────────────────┐
│      Frontend (Node.js)         │
│         Port: 3000              │
└──────────────┬──────────────────┘
               │ calls internally via HTTP
    ┌──────────┴──────────────┐
    │                         │
    ▼                         ▼
Product Service (Go)    Cart Service (Python)
    Port: 8080              Port: 8081
    │                         │
    ▼                         ▼
Order Service (Java)    Payment Service (C#)
    Port: 8082              Port: 8083
                              │
                              ▼
                  Notification Service (Python)
                          Port: 8084
```

## 🛠️ Tech Stack

| Service | Language | Framework | Port |
|---|---|---|---|
| Frontend | Node.js | Express + EJS | 3000 |
| Product Service | Go | net/http | 8080 |
| Cart Service | Python | Flask | 8081 |
| Order Service | Java | Spring Boot | 8082 |
| Payment Service | C# | ASP.NET Core | 8083 |
| Notification Service | Python | Flask | 8084 |

## 🔄 CI/CD Pipeline

Each service has its own independent GitHub Actions workflow:

```
Code pushed to main
        ↓
1. Build & Test
   ├── Install dependencies
   ├── Run unit tests
   └── Code quality check
        ↓
2. Security Scan (Trivy)
   ├── Scan Docker image for CVEs
   └── Upload results to GitHub Security tab
        ↓
3. Docker Build & Push
   ├── Build image
   ├── Tag with run_id (traceability)
   └── Push to DockerHub
        ↓
4. Update K8s Manifests
   ├── Update image tag in retrogame-k8s-manifests
   └── Open Pull Request for review
        ↓
5. ArgoCD Auto Sync
   └── Deploys new version to EKS on PR merge
```

### Workflows per Service

| Service | Workflow | Test Tool | Lint Tool |
|---|---|---|---|
| Frontend | `frontend-ci.yaml` | npm test | ESLint |
| Product Service | `product-service-ci.yaml` | go test | golangci-lint |
| Cart Service | `cart-service-ci.yaml` | pytest | Ruff |
| Order Service | `order-service-ci.yaml` | mvn test | Checkstyle |
| Payment Service | `payment-service-ci.yaml` | dotnet test | dotnet format |
| Notification Service | `notification-service-ci.yaml` | pytest | Ruff |

## 🔒 Security Scanning with Trivy

Every Docker image is scanned for vulnerabilities before pushing to DockerHub:

```yaml
- name: Run Trivy vulnerability scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ${{ env.IMAGE_NAME }}
    format: 'sarif'
    output: 'trivy-results.sarif'
    severity: 'CRITICAL,HIGH'

- name: Upload scan results to GitHub Security tab
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: 'trivy-results.sarif'
```

Results are visible in the **Security tab** of this repository.

## 🚀 Running Locally with Docker Compose

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Steps

**1. Clone the repository:**
```bash
git clone https://github.com/Edwin-Oghenetejiri1/retrogame-microservices-k8s.git
cd retrogame-microservices-k8s
```

**2. Start all services:**
```bash
docker-compose up --build
```

**3. Access the application:**
```
http://localhost:3000
```

### Individual Service URLs

| Service | URL |
|---|---|
| Frontend | http://localhost:3000 |
| Product Service | http://localhost:8080 |
| Cart Service | http://localhost:8081 |
| Order Service | http://localhost:8082 |
| Payment Service | http://localhost:8083 |
| Notification Service | http://localhost:8084 |

### Stop all services
```bash
docker-compose down
```

## 🐳 Docker Images

All images are available on DockerHub with two tags:
- `:latest` — most recent build
- `:<run_id>` — specific build for traceability and rollback

| Service | Image |
|---|---|
| Frontend | `oghenetejiri798/frontend:latest` |
| Product Service | `oghenetejiri798/product-service:latest` |
| Cart Service | `oghenetejiri798/cart-service:latest` |
| Order Service | `oghenetejiri798/order-service:latest` |
| Payment Service | `oghenetejiri798/payment-service:latest` |
| Notification Service | `oghenetejiri798/notification-service:latest` |

## 📁 Repository Structure

```
retrogame-microservices-k8s/
├── src/
│   ├── frontend/                  # Node.js + Express + EJS
│   │   ├── app.js
│   │   ├── views/
│   │   ├── Dockerfile
│   │   └── package.json
│   ├── product-service/           # Go
│   │   ├── main.go
│   │   └── Dockerfile
│   ├── cart-service/              # Python + Flask
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── order-service/             # Java + Spring Boot
│   │   ├── src/
│   │   ├── pom.xml
│   │   └── Dockerfile
│   ├── payment-service/           # C# + ASP.NET Core
│   │   ├── Program.cs
│   │   └── Dockerfile
│   └── notification-service/      # Python + Flask
│       ├── main.py
│       ├── requirements.txt
│       └── Dockerfile
├── .github/
│   └── workflows/
│       ├── frontend-ci.yaml
│       ├── product-service-ci.yaml
│       ├── cart-service-ci.yaml
│       ├── order-service-ci.yaml
│       ├── payment-service-ci.yaml
│       └── notification-service-ci.yaml
└── docker-compose.yaml
```

## 🔗 Related Repositories

- [RetroGame K8s Manifests](https://github.com/Edwin-Oghenetejiri1/retrogame-k8s-manifests) — Kubernetes deployment manifests managed by ArgoCD
- [RetroGame EKS Infrastructure](https://github.com/Edwin-Oghenetejiri1/retrogameshop-eks-infra) — Terraform EKS infrastructure with GitHub Actions CI/CD
```

---

**To add Trivy scanning to your existing CI workflows**, add these two steps after Docker build and before push in each workflow:

```yaml
      - name: Run Trivy vulnerability scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ secrets.DOCKER_USERNAME }}/${{ env.APP_NAME }}:${{ github.run_id }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
        continue-on-error: true

      - name: Upload Trivy scan results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
        continue-on-error: true
```
