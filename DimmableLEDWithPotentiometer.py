from machine import Pin,ADC,PWM
from time import sleep
LEDPin=15
potentiometerPin=28
myPotentiometer=ADC(potentiometerPin)
LEDobject=PWM(Pin(LEDPin))
LEDobject.freq(1000)
LEDobject.duty_u16(0)
while True:
    potentiometerValue=myPotentiometer.read_u16()
    exponentValue=(16/65550)*potentiometerValue
    brightness=(2)**exponentValue
    #LEDobject.duty_u16(int(potentiometerValue))
    print(potentiometerValue,exponentValue,brightness)
    LEDobject.duty_u16(int(brightness))
