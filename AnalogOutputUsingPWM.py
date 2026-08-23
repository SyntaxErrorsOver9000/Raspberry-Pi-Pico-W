from machine import PWM, Pin
from time import sleep
outPin=16
analogOut=PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)
while True:
    myVoltage=float(input("What voltage would you like? "))
    PWMval = (65535/3.13)*myVoltage
    analogOut.duty_u16(int(PWMval))
    sleep.(.1)
