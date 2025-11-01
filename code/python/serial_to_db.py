import serial
import sqlite3
from datetime import datetime
import time
import sys

# Configuration
SERIAL_PORT = 'COM3'  # Change to '/dev/ttyUSB0' on Linux or '/dev/ttyACM0' on macOS
BAUD_RATE = 9600
DB_FILE = 'data.db'

def init_database():
    """Initialize SQLite database with readings table"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            air_quality INTEGER,
            temperature INTEGER,
            humidity INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized")

def save_reading(air_quality, temperature, humidity):
    """Save sensor reading to database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO readings (air_quality, temperature, humidity)
        VALUES (?, ?, ?)
    ''', (int(air_quality), int(temperature), int(humidity)))
    
    conn.commit()
    conn.close()

def read_serial_data():
    """Read data from Arduino via serial port"""
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud")
        time.sleep(2)  # Wait for Arduino to reset
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                
                if line and line != "Smart Air Monitor Ready":
                    try:
                        # Parse CSV data
                        parts = line.split(',')
                        if len(parts) == 3:
                            air_quality, temperature, humidity = parts
                            save_reading(air_quality, temperature, humidity)
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            print(f"[{timestamp}] Air Quality: {air_quality} PPM | Temp: {temperature}°C | Humidity: {humidity}%")
                    except ValueError:
                        print(f"Error parsing: {line}")
    
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
        print("Make sure Arduino is connected and COM port is correct")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        ser.close()
        sys.exit(0)

if __name__ == "__main__":
    init_database()
    read_serial_data()
