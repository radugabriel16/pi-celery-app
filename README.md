# ⚙️ Async π Calculator

A small Python web API that calculates π with the desired number of decimal digits using Celery
for asynchronous background processing and Redis as a message broker.
The application is designed for easy extension with clean architecture principles — it features
modularized code structure, proper exception handling, and clear separation of concerns between API
endpoints, background tasks, and utility logic.

---

## 🎯 Endpoints

- **/calculate_pi?n=`<number>`**
    -> Starts async computation for `<number>` digits of π --- returns JSON with the generated task_id
- **/check_progress?task_id=`<id>`**
    → Checks the current state, progress, and result of the given task

---

## 🚀 Features

- Built with **Celery + Redis** for distributed task processing
- Runs entirely with **Docker Compose** — no local setup required

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Flask**
- **Celery**
- **Redis**
- **Docker & docker-compose**

---

## ⚙️ Installation & Running

### 1. Clone the repo
```bash
git clone https://github.com/radugabriel16/pi-celery-app.git
```

### 2️. Build and start the application
**Note:** Make sure Docker is installed and running on your system before starting the application.
```bash
docker compose up --build
```

Homepage → [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧹 Cleanup

To stop and remove all running containers:
```bash
docker-compose down
```