# 🍔 Food Delivery Application – Three-Tier DevOps Deployment

## 📌 Overview

This project demonstrates a three-tier food delivery application deployed using modern DevOps tools and practices. It includes frontend, backend, and database layers with containerization, orchestration, and monitoring.

---

## 🚀 Features

* 🍔 Food delivery application (demo system)
* 🧱 Three-tier architecture (Frontend, Backend, Database)
* 🐳 Containerization using Docker
* ☸️ Deployment using Kubernetes
* 📊 Monitoring with Prometheus and Grafana
* 🔁 CI/CD pipeline concept for automated delivery
* ⚡ Scalable and modular architecture

---

## 🛠️ Tech Stack

* Python (Flask) – Backend
* HTML/CSS – Frontend
* SQLite / Database
* Docker
* Kubernetes
* Prometheus
* Grafana

---

## 📂 Project Structure

food-delivery-devops/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   └── prometheus.yml
│
└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/vyshalipl/food-delivery-devops.git

### 2. Navigate to project

cd food-delivery-devops

---

## ▶️ Run using Docker

### Build images

docker build -t food-backend ./backend
docker build -t food-frontend ./frontend

### Run containers

docker run -d -p 5000:5000 food-backend
docker run -d -p 8080:80 food-frontend

---

## ☸️ Kubernetes Deployment

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

---

## 📊 Monitoring

* Prometheus is used to collect metrics
* Grafana is used for visualization

---

## 🔄 CI/CD Concept

This project follows CI/CD principles:

* Continuous Integration for building images
* Continuous Delivery for deployment
* Automated pipeline (conceptual implementation)


---

## 🔒 DevOps Concepts Used

* Containerization
* Microservices architecture
* Orchestration
* Monitoring & Logging
* Continuous Integration / Continuous Delivery

---

## 🚀 Future Enhancements

* Integrate Jenkins for real CI/CD pipeline
* Deploy on AWS / GCP
* Add real database (MySQL/PostgreSQL)
* Improve UI using React

---

## 👩‍💻 Author

Vyshali 

---

## 📜 License

This project is for educational purposes.
