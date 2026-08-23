from machine import Pin
from time import sleep

LED1 = Pin (15, Pin.OUT)
LED2 = Pin (14, Pin.OUT)
LED3 = Pin (13, Pin.OUT)
LED4 = Pin (12, Pin.OUT)

while True:
    LED1.value(0)
    LED2.value(0)
    LED3.value(0)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(0)
    LED3.value(0)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(0)
    LED3.value(1)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(0)
    LED3.value(1)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(1)
    LED3.value(0)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(1)
    LED3.value(1)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(0)
    LED2.value(1)
    LED3.value(1)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(0)
    LED3.value(0)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(0)
    LED3.value(0)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(0)
    LED3.value(1)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(0)
    LED3.value(1)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(1)
    LED3.value(0)
    LED4.value(0)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(1)
    LED3.value(0)
    LED4.value(1)
    sleep (.5)
    
    LED1.value(1)
    LED2.value(1)
    LED3.value(1)
    LED4.value(0)
    sleep (.5)
