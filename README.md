Python Flask API: Containerized for Kubernetes
This project demonstrates a production-ready containerization of a Python Flask application. It is designed to be easily deployed into a Kubernetes cluster, featuring environment-based configuration and health-check endpoints for automated monitoring.
🚀 Key Features
Dockerized: Multi-stage ready architecture.
Health Checks: Includes a /health endpoint for Kubernetes Liveness/Readiness probes.
Lightweight: Based on the python:3.9-slim image to reduce attack surface and deployment time.
Scalable: Stateless design, ready for horizontal scaling.
🛠 Prerequisites
Docker installed (version 20.10+ recommended)
Python 3.9+ (for local development)
📦 How to Build and Run
1. Build the Docker Image
docker build -t flask-k8s-app:v1.0 .


2. Run the Container
docker run -d -p 5000:5000 --name web-app flask-k8s-app:v1.0


3. Verify the Deployment
Open your browser or use curl:
Main API: http://localhost:5000/
Health Check: http://localhost:5000/health
🏗 DevOps Context (Why this is here)
This repository serves as a baseline for CI/CD pipelines. The application structure allows:
Continuous Integration: Automated linting and image building.
Continuous Deployment: Ready to be deployed using Helm charts or standard K8s manifests.
Monitoring: The /health route allows monitoring tools (like Prometheus) to track application uptime.
📜 Commands Summary
Action	Command
Build | docker build -t flask-k8s-app .
Run | docker run -p 5000:5000 flask-k8s-app
Stop | docker stop web-app
Logs | docker logs web-app
