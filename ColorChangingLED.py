from machine import PWM,Pin
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
    myColor=input("What color do you want? ")
    if myColor == "red":
        redBright=65550
        greenBright=0
        blueBright=0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "green":
        redBright=0
        greenBright=65550
        blueBright=0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "blue":
        redBright=0
        greenBright=0
        blueBright=65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "cyan":
        redBright=65550
        greenBright=20000
        blueBright=5000
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "purple":
        redBright=65550
        greenBright=0
        blueBright=65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "yellow":
        redBright=65550
        greenBright=65550
        blueBright=0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "orange":
        redBright=65550
        greenBright=7000
        blueBright=0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
    if myColor == "white":
        redBright=65550
        greenBright=65550
        blueBright=65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
