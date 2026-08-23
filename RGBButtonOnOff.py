from machine import Pin
from time import sleep
redPinButton=13
greenPinButton=14
bluePinButton=15
redPinLED=16
greenPinLED=17
bluePinLED=18
redButton=Pin(redPinButton,Pin.IN,Pin.PULL_UP)
greenButton=Pin(greenPinButton,Pin.IN,Pin.PULL_UP)
blueButton=Pin(bluePinButton,Pin.IN,Pin.PULL_UP)
redLED=Pin(redPinLED,Pin.OUT)
greenLED=Pin(greenPinLED,Pin.OUT)
blueLED=Pin(bluePinLED,Pin.OUT)
redButtonStateNow=0
greenButtonStateNow=0
blueButtonStateNow=0
redButtonStateOld=0
greenButtonStateOld=0
blueButtonStateOld=0
redLEDstate=False
greenLEDstate=False
blueLEDstate=False
while True:
    redButtonStateNow=redButton.value()
    greenButtonStateNow=greenButton.value()
    blueButtonStateNow=blueButton.value()
    print(redButtonStateNow,greenButtonStateNow,blueButtonStateNow)
    sleep(.1)
    if redButtonStateOld==0 and redButtonStateNow==1:
        redLEDstate=not redLEDstate
        redLED.value(redLEDstate)
    redButtonStateOld=redButtonStateNow
    print ('RED',redLEDstate)
    if greenButtonStateOld==0 and greenButtonStateNow==1:
        greenLEDstate=not greenLEDstate
        greenLED.value(greenLEDstate)
    greenButtonStateOld=greenButtonStateNow
    print('GREEN',greenLEDstate)
    if blueButtonStateOld==0 and blueButtonStateNow==1:
        blueLEDstate=not blueLEDstate
        blueLED.value(blueLEDstate)
    blueButtonStateOld=blueButtonStateNow
    print('BLUE',blueLEDstate)
    print(redButtonStateNow,greenButtonStateNow,blueButtonStateNow)
    sleep(.1)
