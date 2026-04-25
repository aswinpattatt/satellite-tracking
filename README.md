# Real-Time Satellite Tracking System

## Overview
This project is a Python-based real-time satellite tracking system that visualizes the live position of satellites on a world map. It uses TLE (Two-Line Element) data to compute satellite positions and updates them dynamically at regular intervals.

## Key Features
- Real-time satellite position tracking using live TLE data  
- Geospatial visualization on a world map  
- Automatic updates at fixed intervals (10 seconds)  
- Latitude & longitude tracking with timestamp logging  
- Visual representation using animated plotting  

## Tools & Technologies
- Python  
- NumPy  
- Matplotlib (Animation)  
- Basemap (Geospatial Visualization)  
- Skyfield (Satellite Tracking & TLE Data)  

## Data Source
- Live satellite data fetched from **Celestrak (TLE Data)**

## Methodology

### 1. Data Acquisition
- Retrieved real-time TLE data from Celestrak  
- Loaded satellite dataset using Skyfield  

### 2. Satellite Position Calculation
- Computed satellite subpoint (latitude & longitude)  
- Used current time for real-time tracking  

### 3. Visualization
- Plotted world map using Basemap  
- Displayed satellite as a moving point  
- Updated position dynamically using Matplotlib animation  

### 4. Real-Time Updates
- System refreshes every 10 seconds  
- Displays live coordinates in console output  

## Output
- Live animated world map showing satellite movement  
- Console logs with timestamp, latitude, and longitude  

## Sample Output
