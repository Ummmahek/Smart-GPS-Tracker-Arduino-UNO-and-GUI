import serial
import time
import folium
import tkinter as tk
from tkinter import Label
from threading import Thread
import webbrowser
import pynmea2

# Set the correct port for your system
ser = serial.Serial('COM3', 9600, timeout=1)  # Change 'COM3' as needed
time.sleep(2)  # Wait for the serial connection to stabilize

map_file = "current_location.html"
browser_opened = False  # Flag to open browser only once

def convert_to_decimal(degrees, direction):
    decimal = degrees // 100 + (degrees % 100) / 60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# Function to parse NMEA and extract lat/lon
def extract_coordinates(nmea_sentence):
    try:
        msg = pynmea2.parse(nmea_sentence)
        if isinstance(msg, pynmea2.GGA) or isinstance(msg, pynmea2.RMC):
            lat = convert_to_decimal(float(msg.lat), msg.lat_dir)
            lon = convert_to_decimal(float(msg.lon), msg.lon_dir)
            return lat, lon
    except Exception as e:
        print(f"Error parsing NMEA: {e}")
    return None, None

# Function to update and display the map
def update_map(lat, lon):
    global browser_opened
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="Your Location").add_to(m)
    m.save(map_file)
    
    if not browser_opened:
        webbrowser.open(map_file)
        browser_opened = True

# Function to safely update Tkinter UI
def update_labels(lat, lon):
    lbl_lat.config(text=f"Latitude: {lat:.6f}")
    lbl_lon.config(text=f"Longitude: {lon:.6f}")

# Read from GPS and update UI
def read_gps():
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("$GNGGA") or line.startswith("$GNRMC"):
                print(f"Received: {line}")
                lat, lon = extract_coordinates(line)
                if lat is not None and lon is not None:
                    root.after(0, update_labels, lat, lon)
                    update_map(lat, lon)
        except Exception as e:
            print(f"Error: {e}")

# Initialize Tkinter UI
root = tk.Tk()
root.title("GPS Location Tracker")

lbl_title = Label(root, text="GPS Location Tracker", font=("Arial", 18, "bold"))
lbl_title.pack(pady=10)

lbl_lat = Label(root, text="Latitude: Waiting...", font=("Arial", 14))
lbl_lat.pack(pady=5)

lbl_lon = Label(root, text="Longitude: Waiting...", font=("Arial", 14))
lbl_lon.pack(pady=5)

# Start the GPS thread
gps_thread = Thread(target=read_gps, daemon=True)
gps_thread.start()

root.mainloop()