// Smart Air Monitoring System - Arduino UNO
// Sensors: MQ135 (A0), DHT11 (D2)
// Sends data via Serial: air_quality,temperature,humidity

#include <DHT.h>

#define DHT_PIN 2
#define MQ135_PIN A0
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

// MQ135 calibration
const float MQ135_RO = 10000.0;  // Sensor resistance in fresh air
const float CALIBRATION_SAMPLE_TIMES = 50;
const float CALIBRATION_SAMPLE_INTERVAL = 0.1;
const float READ_SAMPLE_TIMES = 5;
const float READ_SAMPLE_INTERVAL = 0.04;

float RS_O;

// Calculate RS value from ADC value
float MQResistanceCalculation(int rawADC) {
  return ((1023.0 / (float)rawADC) - 1.0) * 10000.0 / 4.99;
}

// MQ-135 Calibration
void MQCalibration() {
  float RS = 0;
  for (int i = 0; i < CALIBRATION_SAMPLE_TIMES; i++) {
    RS += MQResistanceCalculation(analogRead(MQ135_PIN));
    delay(CALIBRATION_SAMPLE_INTERVAL * 1000);
  }
  RS_O = RS / CALIBRATION_SAMPLE_TIMES;
  RS_O = RS_O / MQ135_RO;
}

// Read MQ135 value
float MQRead() {
  float RS = 0;
  for (int i = 0; i < READ_SAMPLE_TIMES; i++) {
    RS += MQResistanceCalculation(analogRead(MQ135_PIN));
    delay(READ_SAMPLE_INTERVAL * 1000);
  }
  RS = RS / READ_SAMPLE_TIMES;
  RS = RS / MQ135_RO;
  
  // MQ135 PPM calculation (CO2 equivalent)
  float ppm = 116.6 * pow(RS / RS_O, -2.769);
  return ppm;
}

void setup() {
  Serial.begin(9600);
  delay(2000);  // Wait for sensor stabilization
  
  dht.begin();
  MQCalibration();  // Calibrate MQ135
  
  Serial.println("Smart Air Monitor Ready");
}

void loop() {
  // Read MQ135 air quality
  float airQuality = MQRead();
  
  // Read DHT11 temperature and humidity
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  // Check if DHT read failed
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("ERROR,ERROR,ERROR");
  } else {
    // Send data in CSV format: airQuality,temperature,humidity
    Serial.print((int)airQuality);
    Serial.print(",");
    Serial.print((int)temperature);
    Serial.print(",");
    Serial.println((int)humidity);
  }
  
  delay(2000);  // Send data every 2 seconds
}
