import streamlit as st
from plotly.graph_objs import Bar, Figure
from simulation import get_utility_rate, calculate_savings

st.set_page_config(page_title="Energy Efficiency Simulator", layout="centered")

st.title("🏡 Energy Efficiency Simulator")
st.write("Estimate your energy savings and CO₂ reduction from clean energy upgrades.")

# Input: Monthly energy usage
usage_kwh = st.number_input(
    "Monthly Energy Usage (kWh)",
    min_value=100,
    max_value=5000,
    value=800,
    step=50,
    help="Enter your average monthly electricity usage in kilowatt-hours (kWh)."
)

# Input: State selector
state = st.selectbox(
    "Select your state",
    options=sorted([
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]),
    index=0
)

# Fetch utility rate
rate = get_utility_rate(state)

# Calculate savings and emissions
results = calculate_savings(usage_kwh, rate)

# Display summary
st.subheader("💰 Savings Summary")
st.write(results["summary"])

# Plot monthly costs comparison
fig = Figure()
fig.add_trace(Bar(
    x=["Current Cost", "Solar Cost", "Heat Pump Cost"],
    y=[results["current_cost"], results["solar_cost"], results["heat_pump_cost"]],
    marker_color=["blue", "orange", "green"]
))
fig.update_layout(
    title="Estimated Monthly Energy Costs",
    yaxis_title="USD ($)",
    xaxis_title="Energy Source"
)
st.plotly_chart(fig, use_container_width=True)

# Funding & rebates info
st.markdown("### 🎯 Funding & Rebates")
st.markdown(
    f"For potential rebates and incentives in {state}, visit the [DSIRE database](https://www.dsireusa.org/)."
)

st.markdown("---")
st.markdown("© 2025 Energy Efficiency Simulator | Data sources: EIA, EPA, DSIRE")
