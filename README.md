# Smart Attendance AI Platform

An end-to-end AI-powered Smart Attendance System built using **Deep Learning, MLOps, and DevOps** practices.

The platform performs real-time face recognition using **FaceNet + DeepFace**, tracks attendance automatically, and integrates modern MLOps tools for experiment tracking, reproducibility, CI/CD, and deployment.

---

# Features

- AI-powered face recognition system
- Real-time attendance marking
- FastAPI backend APIs
- Streamlit interactive dashboard
- MLflow experiment tracking
- DVC data & pipeline versioning
- Docker containerization
- Docker Hub image deployment
- GitHub Actions CI/CD pipeline
- Kubernetes deployment manifests
- Modular production-style architecture

---

# Tech Stack

## AI / ML
- DeepFace
- FaceNet
- TensorFlow
- Scikit-learn
- NumPy

## Backend
- FastAPI
- Uvicorn

## Frontend
- Streamlit
- Plotly
- Pandas

## MLOps / DevOps
- MLflow
- DVC
- Docker
- Docker Hub
- GitHub Actions
- Kubernetes
- AWS EC2

---

# Project Architecture

```text
Smart Attendance AI Platform
│
├── frontend/                 # Streamlit frontend
├── src/
│   ├── api/                  # FastAPI routes
│   ├── services/             # Business logic
│   ├── training/             # Embedding generation
│   ├── mlops/                # MLflow integration
│   ├── config/               # Environment settings
│   └── utils/                # Logger and utilities
│
├── data/
│   ├── raw/                  # Dataset
│   └── embeddings/           # Face embeddings
│
├── kubernetes/               # Kubernetes manifests
├── .github/workflows/        # CI/CD pipelines
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── dvc.yaml
└── requirements.txt
```

---

# MLOps Workflow

- Dataset versioning using DVC
- Face embedding generation pipeline
- MLflow experiment tracking
- Recognition metrics logging
- Artifact management
- CI/CD validation using GitHub Actions
- Dockerized deployment workflow

---

# Docker Images

## Backend Image
https://hub.docker.com/r/abhay3082003/smart-attendance-backend

## Frontend Image
https://hub.docker.com/r/abhay3082003/smart-attendance-frontend

---

# Run Backend

```bash
uvicorn src.api.main:app --reload
```

---

# Run Frontend

```bash
streamlit run frontend/app.py
```

---

# Run MLflow

```bash
mlflow ui
```

---

# Docker Build

## Backend

```bash
docker build -t smart-attendance-backend -f Dockerfile.backend .
```

## Frontend

```bash
docker build -t smart-attendance-frontend -f Dockerfile.frontend .
```

---

# CI/CD Pipeline

The project uses GitHub Actions for:

- Dependency validation
- FastAPI verification
- Frontend verification
- MLflow integration checks
- DVC pipeline validation
- Deployment workflow validation

---

# Future Improvements


- Multi-face recognition
- Cloud-native Kubernetes deployment
- Model registry integration
- Monitoring dashboard

---

# Author

Abhay Singh

AI/ML Engineer | MLOps Enthusiast 