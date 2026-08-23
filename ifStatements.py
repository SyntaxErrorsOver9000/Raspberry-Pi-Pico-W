from machine import Pin
from time import sleep
LED = Pin(15, Pin.OUT)

while True:
    CMD = input ("What is your command? (On/Off/Toggle)  ")
    if CMD == "On":
        LED.value (1)
    if CMD == "Off":
        LED.value (0)
    if CMD == "Toggle":
        LED.toggle()
