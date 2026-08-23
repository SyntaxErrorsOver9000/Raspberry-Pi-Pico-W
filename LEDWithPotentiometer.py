import machine
from time import sleep
potPinGPIO26GREEN = 26
potPinGPIO27BLUE = 27
potPinGPIO28RED = 28
myPotentiometerGREEN = machine.ADC(potPinGPIO26GREEN)
myPotentionmeterBLUE = machine.ADC(potPinGPIO27BLUE)
myPotentiometerRED = machine.ADC(potPinGPIO28RED)
voltage = (100/65280) * potValGREEN - (256 * 100 / 65280)
while True:
    potValGREEN = myPotentiometerGREEN.read_u16()
    if voltage >= 95:
        LED.value (1)
    else:
        LED.value (0)
    voltage = (100/65280) * potValGREEN - (256 * 100 / 65280)
    print ("Your voltage is: ", voltage)
    sleep(.5)
