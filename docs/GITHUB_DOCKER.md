# GitHub and Docker Procedure

## GitHub

```bash
git init
git add .
git commit -m "Initial full-stack application"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Docker

Build:

```bash
docker build -t disaster-relief .
```

Run:

```bash
docker run -p 5000:5000 disaster-relief
```

Stop:

```bash
docker ps
docker stop CONTAINER_ID
```
