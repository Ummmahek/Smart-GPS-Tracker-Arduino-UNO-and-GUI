# Smart GPS Tracker using Arduino UNO and Python GUI

This project presents a real-time GPS location tracker using an Arduino UNO, NEO-8M GPS module, Python (Tkinter), and Folium. The system acquires live location data from satellites, visualizes it on a GUI, and dynamically updates the position on a browser-based map.

## System Components

- **Arduino UNO**: Collects NMEA sentences from the GPS module.
- **NEO-8M GPS Module**: Captures real-time latitude and longitude.
- **Python Serial Communication**: Parses GPS data from the Arduino.
- **Tkinter UI**: Displays current GPS coordinates.
- **Folium Map + HTML**: Generates a live map with markers in a browser.
- **Threading**: Ensures UI remains responsive during live updates.

## Features

- Real-time GPS tracking using serial communication.
- Responsive GUI with live latitude and longitude.
- Folium-based map visualization automatically opened in a browser.
- Error handling for invalid GPS signals and communication issues.

## Requirements

- Python 3.x
- Libraries:
  - `pyserial`
  - `pynmea2`
  - `folium`
  - `tkinter` (pre-installed)
  - `threading` (built-in)
  - `webbrowser` (built-in)

Install libraries using:

```bash
pip install pyserial pynmea2 folium
