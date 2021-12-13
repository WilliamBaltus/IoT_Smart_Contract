import adafruit_bme680
import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

def getData():
    temp = bme680.temperature
    gas = bme680.gas
    humidity = bme680.relative_humidity
    pressure = bme680.pressure
    altitude = bme680.altitude
    dataDict = {'Temperature': temp,
                'Gas' :gas,
                'Humidity': humidity,
                'Pressure': pressure,
                'Altitude': altitude}
   
  return(dataDict)

if __name__ == "__main__":
  print(getData())
