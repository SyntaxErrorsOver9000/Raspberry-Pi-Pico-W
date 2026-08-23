from machine import Pin,ADC
from time import sleep
potPin=28 
greenLED=13
blueLED=14
redLED=15
myPot=ADC(potPin)
myGreen=Pin(greenLED,Pin.OUT)
myBlue=Pin(blueLED,Pin.OUT)
myRed=Pin(redLED,Pin.OUT)
myGreen.value(0)
myBlue.value(0)
myRed.value(0)
while True:
    potVal=myPot.read_u16()
    myVal=(100/65295)*potVal-(100*240/65295)
    print(myVal)
    sleep(.1)
    if myVal<80:
        myGreen.value(1)
        myBlue.value(0)
        myRed.value(0)
    if myVal>=80 and myVal<95:
        myGreen.value(0)
        myBlue.value(1)
        myRed.value(0)
    if myVal>=95:
        myGreen.value(0)
        myBlue.value(0)
        myRed.value(1)
