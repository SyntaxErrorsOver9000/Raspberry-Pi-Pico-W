#I couldn't get the toggle button working. Episode 24 Paul McWhorter
from machine import Pin
import utime as time
from dht import DHT11
from lcd1602 import LCD
lcd=LCD()

dataPin=17
myPin=Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor=DHT11(myPin)

buttonPin=16
myButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)
tempUnitC=True
buttonState=1
buttonStateOld=1
print("My Sensor Data")
while True:
    buttonState=myButton.value()
    if buttonStateOld==0 and buttonState==1:
        tempUnitC= not tempUnitC
    try:
        sensor.measure()
    except:
        pass
    tempC=sensor.temperature()
    tempF=tempC*9/5+32
    humidity=sensor.humidity()
    if tempUnitC==True:
        print("\r","Temp= ",tempC,chr(176)+"C   ","Humidity= ",humidity,"%",end="   ")
        lcd.write(0,0,"Temp: "+str(tempC)+"\xDF"+"C")
        lcd.write(0,1,"Humidity: "+str(humidity)+"%")
    if tempUnitC==False:
        print("\r","Temp= ",tempF,chr(176)+"F   ","Humidity= ",humidity,"%",end="   ")
        lcd.write(0,0,"Temp: "+str(tempF)+"\xDF"+F)
        lcd.write(0,1,"Humidity: "+str(humidity)+"%")
    time.sleep(.1)
    buttonStateOld=buttonState
