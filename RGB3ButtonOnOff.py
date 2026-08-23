from machine import Pin
from time import sleep

redButton = Pin(13, Pin.IN, Pin.PULL_UP)
greenButton = Pin(14, Pin.IN, Pin.PULL_UP)
blueButton = Pin(15, Pin.IN, Pin.PULL_UP)

redLED = Pin(16, Pin.OUT)
greenLED = Pin(17, Pin.OUT)
blueLED = Pin(18, Pin.OUT)

redButtonStateOld = 1
greenButtonStateOld = 1
blueButtonStateOld = 1

redLEDstate = False
greenLEDstate = False
blueLEDstate = False

print("Press button)")

while True:
    redButtonStateNow = redButton.value()
    greenButtonStateNow = greenButton.value()
    blueButtonStateNow = blueButton.value()

    if redButtonStateOld == 1 and redButtonStateNow == 0:
        redLEDstate = not redLEDstate
        redLED.value(redLEDstate)
        print("RED:", redLEDstate)
    redButtonStateOld = redButtonStateNow

    if greenButtonStateOld == 1 and greenButtonStateNow == 0:
        greenLEDstate = not greenLEDstate
        greenLED.value(greenLEDstate)
        print("GREEN:", greenLEDstate)
    greenButtonStateOld = greenButtonStateNow

    if blueButtonStateOld == 1 and blueButtonStateNow == 0:
        blueLEDstate = not blueLEDstate
        blueLED.value(blueLEDstate)
        print("BLUE:", blueLEDstate)
    blueButtonStateOld = blueButtonStateNow

    sleep(0.02)
