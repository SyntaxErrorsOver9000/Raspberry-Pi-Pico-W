from machine import Pin
import time
redPin=15
redLED=Pin(redPin,Pin.OUT)
while True:
    blinks=1
    numBlinks=int(input("How many blinks? "))
    print(numBlinks)
    while blinks<=numBlinks:
        redLED.value(1)
        time.sleep(.5)
        redLED.value(0)
        time.sleep(.5)
        blinks=blinks+1
        
use rgb   
ask the user how many different colors do they want to see
the program will ask what's the 1st color, what's the 2nd
    etc
red blue green cyan magenta yellow orange white
