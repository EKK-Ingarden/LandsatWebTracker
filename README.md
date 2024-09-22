# Landsat Web Tracker

Project made by EKK Ingarden for [Nasa Space Apps 2024](https://www.spaceappschallenge.org/).

## Prerequisites
- Node.js
- Pnpm
- Poetry

## Installation
Remember to provide all environment variables in `.env` file!
```bash
pnpm install
```

## Development
Start database
```bash
docker compose up -d
```
Running the project
```bash
# Frontend
pnpm frontend:dev

# Backend
pnpm backend:dev

# Everything
pnpm dev
```