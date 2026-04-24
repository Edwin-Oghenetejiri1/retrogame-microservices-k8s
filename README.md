# 🕹️ RetroGame Microservices

> End-to-end DevOps project | Microservices in 5 languages | Containerized with Docker | Orchestrated with Kubernetes | CI/CD with GitHub Actions | GitOps with ArgoCD

## 📋 Overview

RetroGame Shop is a full-stack e-commerce platform for retro gaming products built as a microservices architecture. This repository demonstrates real-world DevOps practices including containerization, CI/CD pipelines, and cloud-native deployment.

## 🏗️ Architecture

┌─────────────────────────────────────────────────┐
│                   Frontend (Node.js)             │
│                   Port: 3000                     │
└──────────┬──────────────────────────────────────┘
│ calls internally via HTTP
┌──────┴───────────────────────────┐
│                                  │
▼                                  ▼
Product Service (Go)          Cart Service (Python)
Port: 8080                    Port: 8081
│                                  │
▼                                  ▼
Order Service (Java)          Payment Service (C#)
Port: 8082                    Port: 8083
│
▼
Notification Service (Python)
Port: 8084

## 🛠️ Tech Stack

| Service | Language | Framework | Port |
|---|---|---|---|
| Frontend | Node.js | Express + EJS | 3000 |
| Product Service | Go | net/http | 8080 |
| Cart Service | Python | Flask | 8081 |
| Order Service | Java | Spring Boot | 8082 |
| Payment Service | C# | ASP.NET Core | 8083 |
| Notification Service | Python | Flask | 8084 |

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
http://localhost:3000

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

## 🔄 CI/CD Pipeline

Each service has its own GitHub Actions workflow that automatically:

Code pushed to main
↓

Build & Test
├── Install dependencies
├── Run unit tests
└── Check code quality (Ruff/ESLint/golangci-lint)
↓
Code Quality
├── Lint check
└── Format check
↓
Docker Build & Push
├── Build Docker image
└── Push to DockerHub with run_id tag
↓
Update K8s Manifests
├── Update image tag in retrogame-k8s-manifests repo
└── Open Pull Request for review

### Workflows

| Service | Workflow | Language Tools |
|---|---|---|
| Frontend | `frontend-ci.yaml` | ESLint |
| Product Service | `product-service-ci.yaml` | golangci-lint |
| Cart Service | `cart-service-ci.yaml` | Ruff |
| Order Service | `order-service-ci.yaml` | Checkstyle |
| Payment Service | `payment-service-ci.yaml` | dotnet format |
| Notification Service | `notification-service-ci.yaml` | Ruff |

## 🐳 Docker Images

All images are available on DockerHub:

| Service | Image |
|---|---|
| Frontend | `oghenetejiri798/frontend:latest` |
| Product Service | `oghenetejiri798/product-service:latest` |
| Cart Service | `oghenetejiri798/cart-service:latest` |
| Order Service | `oghenetejiri798/order-service:latest` |
| Payment Service | `oghenetejiri798/payment-service:latest` |
| Notification Service | `oghenetejiri798/notification-service:latest` |

## 📁 Repository Structure
retrogame-microservices-k8s/
├── src/
│   ├── frontend/              # Node.js + Express + EJS
│   │   ├── app.js
│   │   ├── views/
│   │   ├── Dockerfile
│   │   └── package.json
│   ├── product-service/       # Go
│   │   ├── main.go
│   │   └── Dockerfile
│   ├── cart-service/          # Python + Flask
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── order-service/         # Java + Spring Boot
│   │   ├── src/
│   │   ├── pom.xml
│   │   └── Dockerfile
│   ├── payment-service/       # C# + ASP.NET Core
│   │   ├── Program.cs
│   │   └── Dockerfile
│   └── notification-service/  # Python + Flask
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

## 🔗 Related Repositories

- [RetroGame K8s Manifests](https://github.com/Edwin-Oghenetejiri1/retrogame-k8s-manifests) — Kubernetes deployment manifests
- [RetroGame EKS Infrastructure](https://github.com/Edwin-Oghenetejiri1/retrogame-eks-infra) — Terraform EKS infrastructure
