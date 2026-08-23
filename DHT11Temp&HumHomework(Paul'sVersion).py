from machine import Pin
import utime as time
from dht import DHT11
#pins NOT pointing to each other will be ground and power
dataPin=16
myPin=Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
sensor=DHT11(myPin)
buttonPin=15
myButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)
tempUnitC=True
buttonState=1
buttonStateOld=1
print("My Sensor Data")

while True:
    
    
    buttonState=myButton.value
    #the above is to read the button input
    #buttonState 1 is up, 0 is down
    if buttonStateOld==0 and buttonState==1:
        tempUnitC=not tempUnitC
    sensor.measure()
    Humidity=sensor.humidity()
    #the above tells it to take a measurement but it doesn't return it like print
    tempC=sensor.temperature()
    tempF=tempC*9/5+32
    if tempUnitC==True:
        print("\r",'Temperature= ',tempC, chr(176)+'C', 'Humidity= ',Humidity,'%',end='      ')
    if tempUnitC==False:
        tempC=sensor.temperature()
    tempUnitF=tempC*9/5+32
    if tempUnitF==True:
        print("\r",'Temperature= ',tempF, chr(176)+'F', 'Humidity= ',Humidity,'%',end=' ')
    time.sleep(.2)
    buttonStateOld=buttonState
