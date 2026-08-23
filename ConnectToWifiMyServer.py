#connect to pi
import socket
import time
import network

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
    dataString=("WE RECEIVED YOUR COMMAND: "+messageDecoded)
    dataStringEncoded=dataString.encode("utf-8")
    UDPServer.sendto(dataStringEncoded,address)
