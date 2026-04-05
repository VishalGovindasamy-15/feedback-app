#  Feedback Management System (Dockerized)

##  Project Overview

This project is a **Dockerized Feedback Management System** built using **Python (Flask)** and **PostgreSQL**.

It allows users to:

* Register and log in
* Create custom feedback forms
* Share forms via link
* Collect and view responses securely

The entire system is containerized using **Docker** and managed with **Docker Compose**, making it easy to run and deploy.

---

##  Objectives

* Learn Docker fundamentals through a real-world project
* Understand multi-container applications
* Implement backend + database integration
* Practice API development with Flask
* Build a portfolio-ready DevOps project

---

##  Tech Stack

###  Backend

* Python 3
* Flask (Web framework)
* Flask-Login (Authentication)
* Flask-SQLAlchemy (ORM)

###  Database

* PostgreSQL (Docker container)

###  DevOps

* Docker
* Docker Compose

---

##  Features

###  User Management

* User registration
* Secure login/logout
* Session handling

###  Feedback Form System

* Create custom feedback forms
* Add dynamic fields (text, number, etc.)
* Generate unique form links

###  Response Management

* Submit responses via shared link
* Store responses in database
* View responses (only by form creator)

###  Security

* User-based access control
* Only creators can view their data

---

##  Project Architecture

```
                ┌────────────────────┐
                │    Flask App       │
                │ (Backend + UI)     │
                └─────────┬──────────┘
                          │
                          │ (Docker Network)
                          ▼
                ┌────────────────────┐
                │   PostgreSQL DB    │
                │   (Container)      │
                └────────────────────┘
```

---

##  Project Structure

```
feedback-app/
│
├── app/
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   ├── templates/
│   └── static/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

##  Docker Setup

###  Dockerfile

Defines the Python environment and installs dependencies.

###  Docker Compose

Runs:

* Flask app container
* PostgreSQL container

###  Volume Usage

* Persist database data even if container stops

---

##  Getting Started

### 1 Clone Repository

```bash
git clone https://github.com/VishalGovindasamy-15/feedback-app.git
cd feedback-app
```

### 2 Create `.env` File

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=feedback_db
```

### 3 Build & Run Containers

```bash
docker-compose up --build
```

### 4 Access Application

```
http://localhost:5000
```

---

##  Useful Docker Commands

### Stop Containers

```bash
docker-compose down
```

### View Running Containers

```bash
docker ps
```

### Rebuild Containers

```bash
docker-compose up --build
```

---

##  Docker Hub (Optional)

Push your image:

```bash
docker build -t yourusername/feedback-app .
docker push yourusername/feedback-app
```

---

##  Future Improvements

* Role-based access (Admin/User)
* Export responses (CSV/Excel)
* Email notifications
* Public deployment (AWS / Render)
* Frontend upgrade (React)

---

##  Learning Outcomes

By completing this project, you will understand:

* Docker image creation
* Container orchestration with Docker Compose
* Backend development with Flask
* Database integration
* Volume and networking in Docker

---

##  Contribution

Feel free to fork and improve this project!

---

##  License

This project is for learning purposes.
