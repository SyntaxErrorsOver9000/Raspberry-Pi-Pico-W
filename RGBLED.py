from machine import Pin,PWM
from time import sleep
redPin=15
greenPin=14
bluePin=13
redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))
redLED.freq(1000)
redLED.duty_u16(0)
greenLED.freq(1000)
greenLED.duty_u16(0)
blueLED.freq(1000)
blueLED.duty_u16(0)
while True:
    #change the brightness amounts to change the color
    redBrightness=0
    greenBrightness=65535
    blueBrightness=0
    
    redLED.duty_u16(redBrightness)
    greenLED.duty_u16(greenBrightness)
    blueLED.duty_u16(blueBrightness)
    sleep(.1)
