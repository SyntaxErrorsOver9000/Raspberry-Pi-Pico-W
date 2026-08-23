from machine import Pin,PWM
from time import sleep
redPin=13
greenPin=14
bluePin=15
redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))
redLED.freq(1000)
greenLED.freq(1000)
blueLED.freq(1000)
redLED.duty_u16(0)
greenLED.duty_u16(0)
blueLED.duty_u16(0)
colorArray=[]
numColors=int(input("How many colors do you want? "))
for i in range(0,numColors,1):
    myColor=input("Enter your color ")
    myColor=myColor.lower()
    colorArray.append(myColor)
    print(colorArray)
while True:
    for color in colorArray:
        if color == "red":
            redBright=65535
            greenBright=0
            blueBright=0
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "green":
            redBright=0
            greenBright=65535
            blueBright=0
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "blue":
            redBright=0
            greenBright=65535
            blueBright=65535
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "purple":
            redBright=65535
            greenBright=0
            blueBright=65535
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "yellow":
            redBright=65535
            greenBright=35000
            blueBright=0
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "orange":
            redBright=65535
            greenBright=10000
            blueBright=0
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
        if color == "off":
            redBright=0
            greenBright=0
            blueBright=0
            redLED.duty_u16(redBright)
            greenLED.duty_u16(greenBright)
            blueLED.duty_u16(blueBright)
            sleep(1)
       
