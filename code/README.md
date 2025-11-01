# Smart Air Monitoring System

A complete IoT project for real-time air quality, temperature, and humidity monitoring using Arduino, Python, and a web dashboard.

## Project Structure

\`\`\`
SmartAirMonitoring/
├── arduino/
│   └── smart_air_monitor.ino
├── python/
│   ├── serial_to_db.py
│   └── app.py
├── web/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── style.css
│   │   └── chart.js
│   └── data.db (auto-generated)
└── README.md
\`\`\`

## Hardware Requirements

- Arduino UNO microcontroller
- MQ135 gas sensor (air quality)
- DHT11 temperature & humidity sensor
- USB cable for serial communication
- Jumper wires and breadboard

## Wiring Diagram

| Component | Pin |
|-----------|-----|
| MQ135 | A0 |
| DHT11 | Digital Pin 2 |
| GND | GND |
| 5V | 5V |

## Software Requirements

- Arduino IDE (for uploading sketch to Arduino)
- Python 3.6+
- Flask
- pyserial
- SQLite3

## Installation & Setup

### 1. Arduino Setup

1. Open Arduino IDE
2. Copy `arduino/smart_air_monitor.ino` code
3. Select Board: Arduino UNO
4. Select the correct COM port
5. Upload the sketch to Arduino

### 2. Python Environment Setup

\`\`\`bash
# Install required packages
pip install flask pyserial

# Navigate to python directory
cd python

# Create database (runs automatically on first execution)
python serial_to_db.py
\`\`\`

### 3. Running the System

**Terminal 1 - Serial Data Reader:**
\`\`\`bash
cd python
python serial_to_db.py
\`\`\`

**Terminal 2 - Flask Web Server:**
\`\`\`bash
cd python
python app.py
\`\`\`

**Open Browser:**
Navigate to `http://127.0.0.1:5000`

## Features

### Dashboard Tab
- Live sensor readings with real-time updates
- Color-coded air quality status (Good/Moderate/Poor)
- Temperature and humidity displays
- Auto-refresh every 5 seconds

### History Tab
- Last 20 sensor readings in table format
- Interactive Chart.js line graph
- Multi-axis visualization:
  - Air Quality (PPM)
  - Temperature (°C)
  - Humidity (%)
- Auto-refresh capability

### About Tab
- Project description
- Hardware components overview
- System workflow
- Technology stack information

## API Endpoints

### GET `/api/data`
Returns the latest sensor reading:
\`\`\`json
{
  "id": 1,
  "timestamp": "2025-01-01T12:00:00",
  "air_quality": 65,
  "temperature": 28,
  "humidity": 60
}
\`\`\`

### GET `/api/history`
Returns last 20 readings in chronological order:
\`\`\`json
[
  {
    "id": 1,
    "timestamp": "2025-01-01T12:00:00",
    "air_quality": 65,
    "temperature": 28,
    "humidity": 60
  }
]
\`\`\`

## Air Quality Index

| Status | Range | Indication |
|--------|-------|-----------|
| Good | < 50 PPM | Excellent air quality |
| Moderate | 50-100 PPM | Acceptable, some caution |
| Poor | > 100 PPM | Air quality is concerning |

## Troubleshooting

### Arduino not connecting
- Check USB cable connection
- Verify COM port in `serial_to_db.py`
- Ensure Arduino drivers are installed

### No data displaying
- Verify Arduino is uploading sensor data
- Check Flask server is running on `http://127.0.0.1:5000`
- Check browser console for JavaScript errors

### Database errors
- Ensure `data.db` has write permissions
- Clear database and restart if corrupted

## Future Enhancements

- Add WiFi connectivity (Arduino MKR WiFi 1010)
- Cloud data storage (Firebase/AWS)
- Mobile app
- Email/SMS alerts for poor air quality
- Data export functionality
- Multi-location monitoring

## License

MIT License - Feel free to use and modify for your projects

## Author

Smart Air Monitoring System v1.0
