# EV Charge Scheduler 🔌

A smart scheduling algorithm that minimizes electric vehicle charging costs by syncing with real-time dynamic electricity pricing and grid demand.

## Description
A smart scheduling algorithm that minimizes electric vehicle charging costs by syncing with real-time dynamic electricity pricing and grid demand.

## Key Features
- **Price-Aware Charging:** Automatically shifts charging sessions to the lowest-cost tariff windows.
- **Battery Health Guard:** Implements charging rate limits to reduce thermal stress on lithium-ion cells.
- **Grid-Friendly Integration:** Supports Demand Response events to pause charging during peak grid strain.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, NumPy, Pandas, Plotly
- **Model:** Heuristic cost-minimization algorithm using time-series price data.

## Engineering Logic
- **Backend:** The scheduler pulls a 24-hour pricing forecast and solves a constrained optimization problem to find the cheapest continuous or staggered charging slots.
- **Software Engine:** A Streamlit dashboard visualizes the "Charging Roadmap," comparing the cost of immediate charging versus the optimized scheduled session.
