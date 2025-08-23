# Multi-Satellite Tracker with AI (Streamlit App)

🚀 Live Demo: [Open in Streamlit](https://7iygu4txtr5yrvuvhn7yqy.streamlit.app/)

This Streamlit app lets you track multiple satellites in real time and predict their future positions using a simple AI model (Linear Regression). It fetches live satellite data from CelesTrak and allows the user to select from a list of popular Earth-orbiting satellites.

---

##  Features

-  Choose from several real satellites (ISS, Hubble, NOAA, Terra, Aqua, Landsat 8)
-  Fetches real-time TLE (Two-Line Element) data from CelesTrak
-  Calculates hourly positions of the selected satellite over 24 hours
-  Trains an AI model (Linear Regression) to predict the 24th hour location
-  Displays the predicted location on a map

---

##  How It Works

1. **Satellite Selection** – Choose a satellite from a dropdown
2. **TLE Data Fetch** – Downloads fresh TLE data using the NORAD ID
3. **Position Calculation** – Uses Skyfield to calculate positions for each hour
4. **AI Prediction** – Trains a linear regression model using 23 hours of data to predict the 24th hour
5. **Map Output** – Displays the predicted satellite position on an interactive map

---

## 🔍 Code Breakdown

###  1. Fetching TLE Data
```python
url = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle"
response = requests.get(url)
tle_data = response.text.strip().split("\n")
```
- Downloads TLE data for the ISS from **CelesTrak**
- TLE lines are used to calculate satellite orbits

---

###  2. Compute Satellite Positions
```python
sat = EarthSatellite(line1, line2, name, ts)
times = [ts.utc(2025, 2, 16, h) for h in range(24)]
positions = [sat.at(t).subpoint() for t in times]
```
- Uses **Skyfield** to calculate the ISS's position for every hour (0–23) on a chosen day
- Converts these into latitude, longitude, and altitude
- Stores the positions in a DataFrame and displays them

---

###  3. Train AI Model
```python
X = np.array(hours[:-1]).reshape(-1, 1)
y_lat = np.array(lats[1:])
y_lon = np.array(lons[1:])
```
- Prepares training data using the last 23 hours
- Trains two **Linear Regression** models:
  - One for predicting **latitude**
  - One for predicting **longitude**

---

###  4. Predict Hour 24 Location
```python
next_hour = np.array([[23]])
pred_lat = model_lat.predict(next_hour)[0]
pred_lon = model_lon.predict(next_hour)[0]
```
- Predicts the ISS's position in hour 24 using the trained models
- Displays the predicted point on a map using `st.map`

---

##  Final Output

- A clean map with the predicted satellite position at hour 24
- A table of hourly ISS positions (lat, lon, altitude)

---

##  How to Run

### Requirements

Install required packages:

```bash
pip install streamlit skyfield scikit-learn pandas requests
```

###  Run the App

```bash
streamlit run app.py
```

---

##  Deploy to Streamlit Cloud

1. Upload this project to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Connect to your GitHub
5. Set the entry file to `app.py`
6. Click **Deploy**

---

##  Technologies Used

- Python 
- Streamlit 
- Skyfield 
- Scikit-learn 
- Pandas & NumPy 

---

##  Why It's Useful

- Learn how real satellite data is tracked and modeled
- Great example of combining **space tech + AI**
- Simple enough for beginners, powerful enough for demos


