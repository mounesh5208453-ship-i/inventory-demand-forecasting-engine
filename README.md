# 📦 Smart Inventory Demand Forecasting Engine

An interactive, containerized data science portfolio application built to predict stockout risks, calculate automated reorder schedules, and provide deep-dive SKU analytics.

## 🚀 Key Features
* **Real-Time Stockout Prediction:** Computes estimated days until stockout based on current stock levels and daily consumption rates.
* **Interactive Search Filtering:** Instantly filter inventory data by specific SKUs.
* **Deep-Dive SKU Modals:** Clickable Bootstrap UI cards that trigger interactive modal overlays with comprehensive analytics.
* **Containerized Architecture:** Fully dockerized for seamless cross-platform deployment.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Pandas, NumPy
* **Frontend:** HTML5, Bootstrap 5, JavaScript (Fetch API)
* **Deployment & Containerization:** Docker, Git / GitHub
## 🏃‍♂️ Quick Start (Running via Docker)

1. Open your terminal and run:
👉 [View Repository on GitHub](https://github.com/mounesh5208453-ship-i/inventory-demand-forecasting-engine)
git clone https://github.com/mounesh5208453-ship-i/inventory-demand-forecasting-engine.git
cd inventory-demand-forecasting-engine
docker build -t inventory-forecast-app .
docker run -d -p 5001:5001 --name inventory-container inventory-forecast-app
