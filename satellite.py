import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap
from skyfield.api import load
from datetime import datetime

# Load TLE data
print("Loading TLE data...")
tle_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle.txt'
satellites = load.tle_file(tle_url)
iss = {sat.name: sat for sat in satellites}['SURCAL 159']
ts = load.timescale()

# Set up the map
fig, ax = plt.subplots(figsize=(12, 6))
m = Basemap(projection='mill',lon_0=0)
m.drawcoastlines()
m.drawcountries()
m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 60.), labels=[0, 0, 0, 1])

# Initialize a moving dot
iss_dot, = m.plot([], [], 'ro', markersize=8, label='Satellite')

plt.title("Live ISS Tracker")
plt.legend(loc='lower left')

# Update function
def update(frame):
    t = ts.now()
    subpoint = iss.at(t).subpoint()
    lat, lon = subpoint.latitude.degrees, subpoint.longitude.degrees

    x, y = m(lon, lat)
    iss_dot.set_data([x],[y])

    print(f"Updated at {datetime.utcnow().strftime('%H:%M:%S')} - Lat: {lat:.2f}, Lon: {lon:.2f}")
    return iss_dot,

# Animate
ani = animation.FuncAnimation(fig, update, interval=10000, blit=False)
plt.show()

#print(f"Current ISS Location -> Latitude: {latitude:.2f}, Longitude: {longitude:.2f}")



'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap
from skyfield.api import load
from datetime import datetime

# Load TLE data
tle_url = 'https://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(tle_url)
iss = {sat.name: sat for sat in satellites}['ISS (ZARYA)']
ts = load.timescale()

# Setup figure and map
fig, ax = plt.subplots(figsize=(12, 6))
m = Basemap(projection='mill', lon_0=0)
m.drawcoastlines()
m.drawcountries()
m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 60.), labels=[0, 0, 0, 1])

# Initialize ISS dot and trail
iss_dot, = m.plot([], [], 'ro', markersize=8, label='ISS')
trail_line, = m.plot([], [], 'y-', linewidth=1.5, alpha=0.7, label='Trail')  # yellow trail line

# Data storage for trail
trail_lons = []
trail_lats = []

plt.title("Real-Time ISS Tracking with Trail")
plt.legend(loc='lower left')

# Update function
def update(frame):
    t = ts.now()
    subpoint = iss.at(t).subpoint()
    lat, lon = subpoint.latitude.degrees, subpoint.longitude.degrees
    x, y = m(lon, lat)
    
    # Update current position
    iss_dot.set_data(x, y)
    
    # Store trail points
    trail_lons.append(lon)
    trail_lats.append(lat)
    
    # Limit trail length (last 50 points)
    if len(trail_lons) > 50:
        trail_lons.pop(0)
        trail_lats.pop(0)
    
    # Convert trail lat/lon to map coordinates
    trail_x, trail_y = m(trail_lons, trail_lats)
    trail_line.set_data(trail_x, trail_y)
    
    print(f"Updated at {datetime.utcnow().strftime('%H:%M:%S')} - Lat: {lat:.2f}, Lon: {lon:.2f}")
    return iss_dot, trail_line

# Animate
ani = animation.FuncAnimation(fig, update, interval=10000, blit=True)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap
from skyfield.api import load
from datetime import datetime
import requests
import tempfile

# Function to fetch TLE data
def fetch_tle_data(url):
    response = requests.get(url)
    return response.text

# Load TLE data
print("Loading TLE data...")
tle_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle.txt'
tle_data = fetch_tle_data(tle_url)

# Create a temporary file to store TLE data
with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
    temp_file.write(tle_data)
    temp_file_path = temp_file.name

# Load the TLE data using Skyfield
satellites = load.tle_file(temp_file_path)
iss = {sat.name: sat for sat in satellites}.get('CALSPHERE 1')

# Check if the satellite was found
if iss is None:
    print("Satellite CALSPHERE 1 not found!")
else:
    print(f"Found satellite: {iss.name}")

# Create timescale object
ts = load.timescale()

# Set up the map
fig, ax = plt.subplots(figsize=(12, 6))
m = Basemap(projection='mill', lon_0=0)
m.drawcoastlines()
m.drawcountries()
m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 60.), labels=[0, 0, 0, 1])

# Initialize a moving dot
iss_dot, = m.plot([], [], 'ro', markersize=8, label='ISS')

plt.title("Live ISS Tracker")
plt.legend(loc='lower left')

# Update function
def update(frame):
    t = ts.now()
    subpoint = iss.at(t).subpoint()
    lat, lon = subpoint.latitude.degrees, subpoint.longitude.degrees

    x, y = m(lon, lat)
    iss_dot.set_data(x, y)

    print(f"Updated at {datetime.utcnow().strftime('%H:%M:%S')} - Lat: {lat:.2f}, Lon: {lon:.2f}")
    return iss_dot,

# Animate
ani = animation.FuncAnimation(fig, update, interval=10000, blit=False)
plt.show()
'''






















