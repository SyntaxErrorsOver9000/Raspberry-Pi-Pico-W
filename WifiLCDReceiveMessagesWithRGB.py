#connect to pi
import socket
import time
import network
import machine
from machine import Pin
from lcd1602 import LCD

redLEDPin=14
greenLEDPin=12
blueLEDPin=10
redLED=Pin(redLEDPin,Pin.OUT)
greenLED=Pin(greenLEDPin,Pin.OUT)
blueLED=Pin(blueLEDPin,Pin.OUT)
redLED.value(0)
greenLED.value(0)
blueLED.value(0)
lcd=LCD()
wifi=network.WLAN(network.STA_IF)
time.sleep(.5)
wifi.activate(True)
time.sleep(.5)
wifi.connect("Starlink","thankselon")
count=0
while wifi.isconnected()==False:
    print("Waiting...")
    lcd.write(0,0,".....Waiting.....")
    lcd.write(0,1,count)
    time.sleep(1)
    count=count+1
    lcd.write(0,0,"0000000000000000")
    lcd.write(0,1,"0000000000000000")
    time.sleep(1)
