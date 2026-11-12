from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)

# Simulated inventory and historical sales dataset
INVENTORY_DATA = [
    {
        "sku": "SKU-101",
        "product_name": "Wireless Noise-Cancelling Headphones",
        "current_stock": 140,
        "daily_demand_rate": 18.5,
        "lead_time_days": 5,
    },
    {
        "sku": "SKU-102",
        "product_name": "Ergonomic Mechanical Keyboard",
        "current_stock": 45,
        "daily_demand_rate": 12.0,
        "lead_time_days": 4,
    },
    {
        "sku": "SKU-103",
        "product_name": "Ultra-Wide 4K Gaming Monitor",
        "current_stock": 20,
        "daily_demand_rate": 8.2,
        "lead_time_days": 7,
    },
    {
        "sku": "SKU-104",
        "product_name": "USB-C Multi-Port Hub",
        "current_stock": 310,
        "daily_demand_rate": 45.0,
        "lead_time_days": 3,
    },
]


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/health")
def health_check():
  return jsonify({"status": "operational", "service": "demand-forecaster"})


@app.route("/api/forecast", methods=["GET"])
def get_forecast():
  df = pd.DataFrame(INVENTORY_DATA)

  # Data Science Calculation: Days until stockout & reorder recommendations
  df["days_until_stockout"] = np.round(
      df["current_stock"] / df["daily_demand_rate"], 1
  )
  df["reorder_recommended"] = df["days_until_stockout"] <= (
      df["lead_time_days"] + 2
  )

  sku_filter = request.args.get("sku")
  if sku_filter:
    df = df[df["sku"].str.upper() == sku_filter.upper()]

  if df.empty:
    return jsonify({"error": f"SKU '{sku_filter}' not found"}), 404

  return jsonify(
      {"total_items_analyzed": len(df), "forecasts": df.to_dict(orient="records")}
  )


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001, debug=True)