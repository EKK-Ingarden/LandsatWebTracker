# 🚀 Landsat Web Tracker

Project made by EKK Ingarden for [Nasa Space Apps 2024](https://www.spaceappschallenge.org/).

__Note: This project was developed as part of a hackathon. While we strived to deliver a functional and engaging application, the code quality may not meet production standards due to time constraints.__


# 📚 Overview

The Landsat Web Tracker bridges the gap between ground-based spectral measurements and Landsat Surface Reflectance (SR) data. By providing users with an intuitive web-based interface, the application makes satellite data more accessible and actionable, fostering environmental awareness and empowering individuals to contribute toward sustainability.
Our solution allows users to:

- Select a target location and time range.
- Receive notifications when Landsat satellites pass over their chosen location.
- Access and visualize Landsat data, including key environmental metrics like temperature, cloud coverage, and Earth-Sun distance.
- Generate reports with advanced metadata, band views, and reflectance analyses.

# 💡 Features

### Landsat Route Tracking

Users can determine when Landsat 8 & 9 will pass over a specific location.

### Data Visualization
Explore satellite imagery and visualize data through various bands such as:

- Temperature
- Agriculture
- Vegetation
- Moisture
- Atmospheric Penetration

### Notifications

Receive email reminders when Landsat flies above selected locations.

### Simplified Data Access

- Skip the complex process of searching and applying for Landsat data.
- Explore curated datasets tailored to your selected conditions.

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

# 🌟 Hackathon

## Challenge

As part of NASA Space Apps 2024, our team tackled the challenge:
“Develop a web-based application that supports the comparison of ground-based observations with Landsat data.”

The objective was to create a solution that enables users to:

- Define a target location.
- Receive notifications when Landsat satellites are scheduled to pass over that location.
- Access and display Landsat Surface Reflectance (SR) data for the corresponding place and time.

## Hackathon Experience

The hackathon was an intense, collaborative, and highly rewarding experience. Over the span of 24 hours, our team:

- Developed a functional prototype to simplify the process of comparing ground-based spectral measurements with Landsat SR data.
- Implemented key features like satellite route tracking, notifications, and data visualization.
- Met a lot of amazing people from various backgrounds, sharing ideas and learning from one another.
- Consumed 19 cups of coffee to keep the energy levels high throughout the event.

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
# Gource

https://github.com/user-attachments/assets/c1c3b7da-9f4d-4ddc-b531-02a951505b03
