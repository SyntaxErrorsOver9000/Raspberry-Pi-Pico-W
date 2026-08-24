#take out cord
#set up a client/server relationship
#RGB LED + LCD1602
#use battery
#put IP address on LCD1602

from machine import Pin
from lcd1602 import LCD
import time
import socket
import network

redPin=14
greenPin=12
bluePin=10
redLED=Pin(redPin,Pin.OUT)
greenLED=Pin(greenPin,Pin.OUT)
blueLED=Pin(bluePin,Pin.OUT)
lcd=LCD()

wifi=network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('Starlink','thankselon')

while wifi.isconnected()==False:
    print("Waiting for connection... ")
    time.sleep(1)
wifiInfo=wifi.ifconfig()
print(wifiInfo)
ServerIP=wifiInfo[0]
ServerPort=2222
#server port # doesn't matter, it will change
bufferSize=1024
#buffer size is the size of the 'package' you'll be sending
#buffer size is measured in bytes
UDPServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#UDP is a communication program
print("UDC Server Up and Waiting... ")
UDPServer.bind((ServerIP,ServerPort))

while True:
    message,address=UDPServer.recvfrom(bufferSize)
    messageDecoded=message.decode("utf-8")
    print("MESSAGE RECEIVED: ",messageDecoded,"FROM: ",address[0])
    dataString=(messageDecoded)
    dataStringEncoded=dataString.encode("utf-8")
    UDPServer.sendto(dataStringEncoded,(address[0],2222))
    lcd.write(0,0,messageDecoded[:16])
    lcd.write(0,1,address[0])
    time.sleep(1)
