import machine
from machine import Pin, Timer
timer = Timer()

LED = Pin("WL_GPIO0", Pin.OUT)

def blink(timer):
    LED.toggle()
    
timer.init(freq = 1, mode = Timer.PERIODIC, callback = blink)
