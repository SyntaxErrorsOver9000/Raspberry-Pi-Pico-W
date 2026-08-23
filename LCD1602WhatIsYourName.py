from lcd1602 import LCD
import utime as time

lcd=LCD()
while True:
    myName=input("What is your name? ")
    lcd.clear()
    greeting1=("Hello "+myName)
    greeting2=("Welcome to my Pi! ")
    lcd.write(0,0,greeting1)
    lcd.write(0,1,greeting2)
