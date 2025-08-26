import streamlit as st
import requests
from skyfield.api import load, EarthSatellite
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")
st.sidebar.title("Satellite Selection")

# Dictionary of satellites with NORAD IDs
satellite_options = {
    "ISS (ZARYA)": "25544",
    "Hubble Space Telescope": "20580",
    "NOAA 19": "33591",
    "Terra": "25994",
    "Aqua": "27424",
    "Landsat 8": "39084"
}

# Satellite selection
selected_sat_name = st.sidebar.selectbox("Choose a satellite:", list(satellite_options.keys()))
selected_norad_id = satellite_options[selected_sat_name]

# Fetch TLE data for the selected satellite
tle_url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={selected_norad_id}&FORMAT=tle"
response = requests.get(tle_url)
tle_data = response.text.strip().split("\n")

name, line1, line2 = tle_data[0], tle_data[1], tle_data[2]

st.title(f" Satellite Tracker with AI")
st.header(f"Tracking: {name}")
st.code(line1)
st.code(line2)

# Step 2: Compute Satellite Positions
st.header("1. Satellite Position Over 24 Hours")
ts = load.timescale()
sat = EarthSatellite(line1, line2, name, ts)
times = [ts.utc(2025, 2, 16, h) for h in range(24)]
positions = [sat.at(t).subpoint() for t in times]

lats = [p.latitude.degrees for p in positions]
lons = [p.longitude.degrees for p in positions]
alts = [p.elevation.km for p in positions]
hours = list(range(24))

df = pd.DataFrame({
    'Hour': hours,
    'Latitude': lats,
    'Longitude': lons,
    'Altitude': alts
})
st.dataframe(df)

# Step 3: Train AI (Linear Regression)
st.header("2. Train AI Model to Predict Hour 24")

X = np.array(hours[:-1]).reshape(-1, 1)
y_lat = np.array(lats[1:])
y_lon = np.array(lons[1:])

model_lat = LinearRegression().fit(X, y_lat)
model_lon = LinearRegression().fit(X, y_lon)

next_hour = np.array([[23]])
pred_lat = model_lat.predict(next_hour)[0]
pred_lon = model_lon.predict(next_hour)[0]

st.success("AI model trained and prediction complete!")

st.subheader("Predicted Satellite Location at Hour 24:")
st.write(f"**Latitude:** `{pred_lat:.2f}°`")
st.write(f"**Longitude:** `{pred_lon:.2f}°`")

# Step 4: Map
st.map(pd.DataFrame({'lat': [pred_lat], 'lon': [pred_lon]}))
