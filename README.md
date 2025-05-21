# Multi-Satellite Tracker with AI (Streamlit App)

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

##  Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

##  How to Run

```bash
streamlit run app_with_satellite_selector.py
```

---

##  Deploying to Streamlit Cloud

1. Upload your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New App" and connect your GitHub repo
4. Set `app_with_satellite_selector.py` as the main file
5. Click **Deploy**

---

##  Technologies Used

- Python
- Streamlit
- Skyfield
- Scikit-learn
- Pandas & NumPy

---
