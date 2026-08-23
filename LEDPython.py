from machine import Pin
from time import sleep

myLED = Pin ("LED", Pin.OUT)

while True:
    myLED (0)
    sleep (.05)
    myLED (0)
    sleep (.05)
