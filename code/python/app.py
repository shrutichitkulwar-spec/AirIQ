from flask import Flask, render_template, jsonify
import sqlite3
from datetime import datetime
import json

app = Flask(__name__, template_folder='../web/templates', static_folder='../web/static')
DB_FILE = 'data.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Serve the main dashboard"""
    return render_template('index.html')

@app.route('/api/data')
def get_latest_data():
    """Return the latest sensor readings"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM readings ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'id': row[0],
            'timestamp': row[1],
            'air_quality': row[2],
            'temperature': row[3],
            'humidity': row[4]
        })
    else:
        return jsonify({
            'id': 0,
            'timestamp': datetime.now().isoformat(),
            'air_quality': 0,
            'temperature': 0,
            'humidity': 0
        })

@app.route('/api/history')
def get_history():
    """Return the last 20 sensor readings"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM readings ORDER BY id DESC LIMIT 20')
    rows = cursor.fetchall()
    conn.close()
    
    readings = []
    for row in reversed(rows):
        readings.append({
            'id': row[0],
            'timestamp': row[1],
            'air_quality': row[2],
            'temperature': row[3],
            'humidity': row[4]
        })
    
    return jsonify(readings)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
