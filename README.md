# 🚀 Landsat Web Tracker

Project made by EKK Ingarden for [Nasa Space Apps 2024](https://www.spaceappschallenge.org/).

https://github.com/user-attachments/assets/c1c3b7da-9f4d-4ddc-b531-02a951505b03

Note: This project was developed as part of a hackathon. While we strived to deliver a functional and engaging application, the code quality may not meet production standards due to time constraints.


# 📚 Overview
The Landsat Web Tracker bridges the gap between ground-based spectral measurements and Landsat Surface Reflectance (SR) data. By providing users with an intuitive web-based interface, the application makes satellite data more accessible and actionable, fostering environmental awareness and empowering individuals to contribute toward sustainability.
Our solution allows users to:

- Select a target location and time range.
- Receive notifications when Landsat satellites pass over their chosen location.
- Access and visualize Landsat data, including key environmental metrics like temperature, cloud coverage, and Earth-Sun distance.
- Generate reports with advanced metadata, band views, and reflectance analyses.
- Download data in PDF and CSV formats.

# 💡 Features

### Landsat Route Tracking
Users can examine satellite routes and determine when Landsat 8 & 9 will pass over a specific location.

### Data Visualization
Explore satellite imagery and visualize data through various bands such as:

- NDVI (Normalized Difference Vegetation Index)
- True Color
- False Color

### Custom Notifications
Receive email reminders when Landsat flies above selected locations.

### Simplified Data Access

- Skip the complex process of searching and applying for Landsat data.
- Download curated datasets tailored to your selected conditions.

### Report Generation
Generate reports containing advanced metadata, band visualizations, and reflectance analyses.

### Environmental Insights
Empower users to explore and understand environmental changes, such as vegetation health, urban expansion, and climate patterns.

# 🎯 Objectives
The Landsat Web Tracker aims to:

- Make high-quality satellite data easily accessible to researchers and enthusiasts.
- Support amateur and professional measurements with easy error correction and calibration.
- Promote informed discussions on environmental issues.
- Encourage interdisciplinary approaches to climate action and urban planning.

# 🛠️ How to setup project

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
