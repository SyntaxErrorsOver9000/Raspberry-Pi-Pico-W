from machine import Pin
import utime as time
from dht import DHT11
dataPin=16
myPin=Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
buttonPin=13
myButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)
sensor=DHT11(Pin(dataPin))

mode=0
buttonState=1
buttonStateOld=1
print("Press the button to cycle data: Temp Celsius, Temp Fahrenheit or Humidity ")

while True:
    buttonState=myButton.value()
    if buttonStateOld==1 and buttonState==0:
        mode=(mode+1)%3
        
        try:
            sensor.measure()
            humidity=sensor.humidity()
        
            if mode==0:
                tempC=sensor.temperature()
                print('\r','It is ',tempC,chr(176)+'C',' in this bitch')
            elif mode==1:
                tempC=sensor.temperature()
                tempF=(tempC*9/5+32)
                print('\r','It is ',tempF,chr(176)+'F',' in this bitch')
            elif mode==2:
                humidity=sensor.humidity()
                print('\r','Humidity is ', humidity)
        except OSError as e:
            print("Sensor read error. Please try again.")
        time.sleep(.3)
    buttonStateOld=buttonState
    time.sleep(.2)
