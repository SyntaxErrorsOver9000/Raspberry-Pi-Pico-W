from machine import Pin
from time import sleep
buttonPin=13
redPin=12

myButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)
redLED=Pin(redPin,Pin.OUT)

buttonStateNow=1
buttonStateOld=0
LEDstate=False
while True:
    buttonStateNow=myButton.value()
    if buttonStateOld==1 and buttonStateNow==0:
        LEDstate=not LEDstate
        redLED.value(LEDstate)
    print(LEDstate,buttonStateNow)
    sleep(.05)
    buttonStateOld=buttonStateNow
    sleep(.05)
