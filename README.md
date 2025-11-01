Smart Air Monitoring System (IoT Project)
 Overview

The Smart Air Monitoring System is an IoT-based project designed to measure and analyze air quality, temperature, and humidity in real time.
It uses Arduino UNO with MQ135 Gas Sensor and DHT11 Sensor, sending data to a Python Flask web dashboard via a USB serial connection.

This project helps monitor environmental health by displaying live readings, historical charts, and alerts for poor air quality.
"https://v0-smart-air-monitoring-system.vercel.app/" This is the link of the working project.
_Features

- Real-time monitoring of air quality, temperature, and humidity
- Dynamic web dashboard with live updates
- History tab with previous readings and charts
- Color indicators for pollution levels
- Data storage in SQLite database
- USB serial communication (no WiFi/ESP module required)
- Simple and responsive UI (Bootstrap/Tailwind)

System Architecture
┌────────────┐       USB Serial       ┌────────────┐      HTTP/JSON      ┌──────────────┐
│  Arduino   │  ───────────────────▶  │  Python    │  ───────────────▶  │  Flask Web   │
│  (Sensors) │                       │  (Bridge)  │                   │  Dashboard   │
└────────────┘                        └────────────┘                   └──────────────┘
        │                                   │                                  │
        │ MQ135  → Air Quality (PPM)        │ Logs data into SQLite database   │
        │ DHT11  → Temperature/Humidity     │ Provides API endpoints           │

-Components Used
Component	Description
Arduino UNO	Main microcontroller
MQ135 Sensor	Measures air quality (CO₂, NH₃, etc.)
DHT11 Sensor	Measures temperature & humidity
USB Cable	For serial communication
Jumper Wires	For connections
Python 3	Serial + Flask backend
Flask	Web dashboard framework
Chart.js	For live graph plotting
SQLite	For data storage
-Workflow

Arduino collects air quality, temperature, and humidity readings.

Data is sent via Serial (USB) every 2 seconds.

Python script reads the serial data, stores it in data.db, and sends it to a Flask server.

Flask Web Dashboard displays:

Dashboard tab: live readings with color indicators

History tab: charts and logs of previous readings

About tab: project info and hardware details

-Folder Structure
SmartAirMonitoring/
│
├── arduino/
│   └── smart_air_monitor.ino
│
├── python/
│   ├── serial_to_db.py
│   └── app.py
│
├── web/
│   ├── templates/
│   │   ├── index.html
│   │   ├── history.html
│   │   └── about.html
│   ├── static/
│   │   ├── style.css
│   │   └── chart.js
│   └── data.db
│
└── README.md

- Installation & Setup
* Step 1: Upload Arduino Code

Open arduino/smart_air_monitor.ino in Arduino IDE.

Select Board: Arduino UNO.

Select your COM port.

Upload the code.

Open the Serial Monitor to check readings (e.g., 45,27,60).

* Step 2: Set Up Python Environment

Install Python 3.

Open terminal and install dependencies:

pip install pyserial flask


Run the serial reader:

python python/serial_to_db.py


This reads Arduino data and stores it in data.db.

* Step 3: Start Flask Server

In another terminal:

python python/app.py


Then open your browser at - http://127.0.0.1:5000

 Website Tabs
Tab	Description
 Dashboard	Live sensor readings with status indicators
 History	Table + Chart.js graph for last 20 readings
 About	Project details and hardware info
 Air Quality Indicators
PPM Range	Status	Color
0–50	Good	🟢 Green
51–100	Moderate	🟡 Yellow
101+	Poor	🔴 Red
 Sample Output

Serial Monitor:

Air: 45 PPM | Temp: 28°C | Humidity: 61%
Air: 78 PPM | Temp: 29°C | Humidity: 59%


Web Dashboard:

Dashboard: Shows live readings

History: Graph of last 20 entries

About: Info about sensors and working

- Future Enhancements

Add email/SMS alerts for poor air quality

Add GPS tracking for location-based data

Add cloud sync (Firebase / Thingspeak)

Add user login and reports export option
