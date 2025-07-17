# Energy Efficiency Simulator

![Energy Efficiency](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80)

**Estimate your home energy savings from clean energy upgrades like solar panels and heat pumps!**

---

## Overview

This project is a simple, interactive **Energy Efficiency Simulator** built with Python and Streamlit. It allows users to:

- Input their monthly home energy usage (kWh)
- Select their U.S. state
- Calculate potential monthly savings on electricity bills from solar panels or heat pumps
- Estimate CO₂ emissions reductions based on EPA data
- Visualize cost comparisons via interactive charts
- Access links to state-specific funding and rebate opportunities via DSIRE

---

## Why This Project?

- Demonstrates clean energy and decarbonization domain knowledge aligned with Uplight’s mission
- Uses public datasets (U.S. Energy Information Administration for rates, EPA for emissions)
- Provides stakeholder-friendly outputs in an interactive web app
- No external API or model dependencies — easy to set up and run locally

---

## Tech Stack

- Python 3.x
- Streamlit (for UI)
- Plotly (for charts)
- Publicly sourced U.S. average utility rates (EIA)
- EPA CO₂ emissions factor

---

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system. It’s recommended to use a virtual environment.

### Installation

1. **Clone this repository:**

git clone https://github.com/yourusername/energy-efficiency-simulator.git
cd energy-efficiency-simulator

2. Create and activate a virtual environment (optional but recommended):

python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. Install dependencies:

pip install -r requirements.txt

## Running the App
Run the Streamlit app locally:

streamlit run app.py
This will start a local web server. Open your browser and go to:

http://localhost:8501
You’ll see the Energy Efficiency Simulator UI.

## How to Use
Enter your average monthly electricity use in kWh.

Select your U.S. state from the dropdown.

The app will display:

Estimated current electricity cost

Potential monthly savings from switching to solar panels or heat pumps

Annual CO₂ emissions reduction in kilograms

An interactive bar chart comparing current vs. solar vs. heat pump monthly costs

Check the link to DSIRE for funding and rebate opportunities in your state.

## Code Highlights
simulation.py: Contains the main calculation functions:

get_utility_rate(state): Returns average electricity rate for a state from publicly sourced data

calculate_savings(usage_kwh, rate): Calculates cost savings and CO₂ reductions

app.py: Streamlit front-end that gathers user inputs and displays results with charts.

##Data Sources
Utility Rates: U.S. Energy Information Administration (EIA) average residential electricity rates per state
https://www.eia.gov/electricity/data/state/

Emissions Factor: EPA average CO₂ emissions per kWh of electricity generation
https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator

Funding & Rebates: DSIRE — comprehensive database of U.S. clean energy incentives
https://www.dsireusa.org/

## Future Improvements
Integrate more granular data for utility rates and emissions factors (e.g., by utility company or zip code)

Add user profiles and history

Include additional clean energy options and calculators (e.g., insulation upgrades, electric vehicles)

Deploy on Streamlit Cloud or other hosting for public access
