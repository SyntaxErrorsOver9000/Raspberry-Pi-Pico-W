from machine import Pin
import time
redPin=15
redLED=Pin(redPin,Pin.OUT)
while True:
    numBlinks=int(input('How many blinks? '))
    print(numBlinks)
    for blink in range(0,numBlinks,1):
        redLED.value(1)
        time.sleep(.5)
        redLED.value(0)
        time.sleep(.5)
