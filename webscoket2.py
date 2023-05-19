import websockets
import asyncio
import serial
import cv2
import numpy
import base64 

box1 = serial.Serial(port = "/dev/ttyACM0",
                    baudrate = 9600,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_NONE,
                    timeout =1)

async def send_message():  
    while True:
        ardRes1 = box1.readline().decode('utf-8')
        print(ardRes1)
        
            
            
asyncio.run(send_message())