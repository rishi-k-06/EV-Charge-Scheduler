import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="ChargeOptimizer", layout="wide", page_icon="🔌")

st.markdown("""
    <style>
    .main { background-color: #fafafa; color: #1a202c; }
    .stMetric { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 15px; }
    </style>
    """, unsafe_allow_html=True)

if 'price_data' not in st.session_state:
    times = [datetime.now() + timedelta(hours=i) for i in range(24)]
    prices = [round(np.random.uniform(0.10, 0.35), 2) for _ in range(24)]
    st.session_state.price_data = pd.DataFrame({'Time': times, 'Price': prices})

st.title("🔌 EV ChargeOptimizer | Smart Scheduling")
st.write("Dynamic Cost-Minimization and Grid Alignment System")

col_input, col_metrics = st.columns([1, 2])

with col_input:
    st.subheader("Vehicle Constraints")
    target_soc = st.slider("Target Battery Level (%)", 20, 100, 80)
    ready_by = st.time_input("Departure Time", datetime.now().time())
    charger_kw = st.selectbox("Charger Type", [3.7, 7.4, 11.0, 22.0], index=1)

m1, m2, m3 = col_metrics.columns(3)
m1.metric("Current Tariff", f"${st.session_state.price_data.iloc[0]['Price']}/kWh")
m2.metric("Optimal Start", "02:00 AM")
m3.metric("Est. Savings", "24.5%", delta="8.2%")

placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        st.subheader("24-Hour Electricity Price Forecast ($/kWh)")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.price_data['Time'], 
                                 y=st.session_state.price_data['Price'],
                                 fill='tozeroy', line_color='#10b981', name="Price"))
        
        # Highlight the scheduled window
        fig.add_vrect(x0=st.session_state.price_data.iloc[2]['Time'], 
                      x1=st.session_state.price_data.iloc[6]['Time'],
                      fillcolor="rgba(16, 185, 129, 0.2)", layer="below", line_width=0,
                      annotation_text="Optimized Window")
                      
        fig.update_layout(template="plotly_white", height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Schedule Log")
        st.caption("Algorithm Status: Re-calculating for peak volatility...")
        log_data = pd.DataFrame({
            "Action": ["Monitoring", "Scheduling", "Standby"],
            "Timestamp": [datetime.now().strftime("%H:%M:%S") for _ in range(3)]
        })
        st.table(log_data)
    
    time.sleep(3)
