# AI381 Lab 2 – Bring Your Own Model: Container + CI

**Course:** AI381 – Machine Learning Operations  
**Instructor:** Dr. Tariq Al-Omari  
**University:** Jordan University of Science and Technology (JUST)  
**Semester:** Fall 2026/27

## Project Overview

This project packages a machine learning churn prediction model as a FastAPI service, runs it inside a Docker container, and automates testing and image publishing using GitHub Actions.

## Project Structure

```text
AI381-Lab2/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app/
│   │   ├── main.py
│   │   └── model.joblib
│   └── train/
│       └── train.py
├── tests/
│   └── test_api.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks whether the API is running |
| POST | `/predict` | Returns the customer's churn probability |

## Run the Project with Docker

Make sure Docker Desktop is running, then execute:

```bash
docker run --rm -p 8000:8000 ghcr.io/taimaafaisal6-tech/ai381-lab2@sha256:c3564b19f813becf3d609c89f4b37e22994be52423d85a4ff0a68244f900af11
```

Open the API documentation:

http://localhost:8000/docs

Health check:

http://localhost:8000/health

## Run Tests Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest tests -v
```

Run lint:

```bash
ruff check src tests
```

## Testing

The project includes seven automated tests covering:

- Health endpoint response.
- Prediction endpoint response.
- Missing input fields.
- Invalid input values.
- Prediction probability range.
- Model loading.
- Deterministic predictions.

## Docker and Security

The Dockerfile uses:

- Multi-stage build.
- A non-root application user.
- A health check.
- Pinned Python dependencies.
- Debian package updates.

Trivy is used in the CI/CD workflow to scan the Docker image for vulnerabilities. Scan findings should be reviewed; a successful workflow does not necessarily mean the image has zero vulnerabilities.

## CI/CD Pipeline

GitHub Actions automatically:

1. Runs Ruff lint checks.
2. Runs the automated tests.
3. Builds the Docker image on pushes to `main`.
4. Scans the image using Trivy.
5. Publishes the image to GitHub Container Registry (GHCR).

The workflow uses GitHub Actions pinned to full commit SHAs.

**GitHub Actions Status:**

[![AI381 CI/CD](https://github.com/taimaafaisal6-tech/AI381-Lab2/actions/workflows/ci.yml/badge.svg)](https://github.com/taimaafaisal6-tech/AI381-Lab2/actions/workflows/ci.yml)

## Published Docker Image

**Image:**

`ghcr.io/taimaafaisal6-tech/ai381-lab2`

**Image Digest:**

`sha256:c3564b19f813becf3d609c89f4b37e22994be52423d85a4ff0a68244f900af11`

## Repository

https://github.com/taimaafaisal6-tech/AI381-Lab2

