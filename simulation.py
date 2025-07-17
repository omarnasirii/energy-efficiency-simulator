
# Average residential electricity rates in USD per kWh by state (sample data)
UTILITY_RATES = {
    "AL": 0.12, "AK": 0.22, "AZ": 0.13, "AR": 0.10, "CA": 0.24,
    "CO": 0.13, "CT": 0.21, "DE": 0.14, "FL": 0.11, "GA": 0.12,
    "HI": 0.33, "ID": 0.09, "IL": 0.13, "IN": 0.12, "IA": 0.11,
    "KS": 0.13, "KY": 0.10, "LA": 0.09, "ME": 0.16, "MD": 0.13,
    "MA": 0.22, "MI": 0.16, "MN": 0.14, "MS": 0.10, "MO": 0.11,
    "MT": 0.11, "NE": 0.11, "NV": 0.12, "NH": 0.20, "NJ": 0.16,
    "NM": 0.11, "NY": 0.20, "NC": 0.12, "ND": 0.10, "OH": 0.13,
    "OK": 0.10, "OR": 0.12, "PA": 0.14, "RI": 0.21, "SC": 0.12,
    "SD": 0.11, "TN": 0.11, "TX": 0.11, "UT": 0.11, "VT": 0.19,
    "VA": 0.12, "WA": 0.10, "WV": 0.11, "WI": 0.15, "WY": 0.11
}

# EPA average emissions factor for US electricity in kg CO2 per kWh (2021 data)
EPA_CO2_EMISSIONS_FACTOR = 0.92  # kg CO2 per kWh (can update as needed)

def get_utility_rate(state_abbr: str) -> float:
    """Return the average residential utility rate for the given state abbreviation."""
    state_abbr = state_abbr.upper()
    return UTILITY_RATES.get(state_abbr, 0.13)  # default average rate if state not found

def calculate_savings(usage_kwh: float, rate: float) -> dict:
    """
    Calculate monthly cost, savings from solar and heat pump,
    and annual CO2 emissions saved.

    Args:
        usage_kwh (float): Monthly energy usage in kWh.
        rate (float): Utility rate in USD per kWh.

    Returns:
        dict: Summary and numeric details of costs and CO2 savings.
    """
    current_cost = usage_kwh * rate
    solar_cost = usage_kwh * 0.02  # Assumed post-solar rate per kWh
    heat_pump_cost = usage_kwh * 0.08  # Assumed heat pump usage rate

    co2_saved = usage_kwh * EPA_CO2_EMISSIONS_FACTOR * 12 / 1000  # annual CO2 saved in metric tons

    summary = (
        f"Your current monthly bill is **${current_cost:.2f}**.\n\n"
        f"Switching to solar could save you **${current_cost - solar_cost:.2f}/mo**\n"
        f"and reduce your CO₂ emissions by **{co2_saved:.1f} kg/year**."
    )

    return {
        "summary": summary,
        "current_cost": current_cost,
        "solar_cost": solar_cost,
        "heat_pump_cost": heat_pump_cost,
        "co2_saved": co2_saved
    }
