#DHT11 Temperature and Humidity Sensor
from machine import Pin
import utime as time
from dht import DHT11

dataPin=16
myPin=Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor=DHT11(myPin)
print('My Sensor Data')
while True:
    sensor.measure()
    tempC=sensor.temperature()
    humidity=sensor.humidity
    print("\r",'Temperature= ',tempC,chr(176)+'C ','Humidity= ',humidity,'%',end='')
    time.sleep(1)
