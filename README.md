# Disaster Relief Resource Coordination Platform

A simple full-stack disaster relief application built for academic demonstration.

## Technology Stack

- Frontend: HTML, CSS, JavaScript/HTML forms
- Backend: Python Flask
- Database: SQLite
- Containerization: Docker
- Version Control: Git and GitHub

## Main Features

1. User login and logout
2. Resource request creation
3. Available resource management
4. Request status update
5. Dashboard
6. REST API endpoint for requests
7. SQLite database
8. Docker deployment

## Demo Login

Email: `admin@example.com`

Password: `admin123`

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Run with Docker

```bash
docker build -t disaster-relief .
docker run -p 5000:5000 disaster-relief
```

Open `http://localhost:5000`.

## GitHub

```bash
git init
git add .
git commit -m "Initial full-stack disaster relief application"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Simple Architecture

User
  |
  v
Frontend (HTML/CSS/JS)
  |
  v
Flask Backend / API
  |
  v
SQLite Database

## Important

For an academic/demo project, replace the Flask secret key before production use and do not commit real passwords or secrets.
