import websockets
import asyncio
import serial
import cv2
import numpy
import base64 
####################################
####### cam location ##############
###################################
#capture1 = cv2.VideoCapture(0)   #
#capture2 = cv2.VideoCapture(2)   #
##################################


########### encoding qultiy#######################
#encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
################################################
###########################################


######### cam qulity setting ##############
############################################
#capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)#
#capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)#
#############################################

########### cam check###########
#if not capture1.isOpened():
#    print('cam1 connect fail')
#    exit()
#if not capture2.isOpened():
#    print('cam2 connect fail')
#    exit()
#################################
    
    
box1 = serial.Serial(port = "/dev/ttyACM1",
                    baudrate = 9600,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_NONE,
                    timeout =1)

#box2 = serial.Serial(port = "/dev/ttyACM0",
#                   baudrate = 9600,
#                    bytesize = serial.EIGHTBITS,
#                    parity = serial.PARITY_NONE,
#                    timeout =1)

async def serial_task(websocket):
    while 1 :
        ardRes1 = box1.readline().decode('utf-8').strip()
        print('from ardu',ardRes1)
        if '1 close' in ardRes1:
            print('websockets sent', ardRes1)
            websocket.send(ardRes1)


async def websocket_task(websocket):
        #await websocket.send((str(len(stringData))).encode().ljust(16) + stringData)
        #print((str(len(stringData))).encode().ljust(16) + stringData)
        while 1:
            # websocket connet and response
            print('socket server')
            res = websocket.recv()            
            print('wait')
            
            
            #ardRes2 = await box1.readline().decode('utf-8')
            print('from server', res)
            if res == '1 open':
                box1.write('1 open'.encode())
                print("box 1 open")
            
                #ret2, frame2 = capture2.read()
                #result, img_encode1 = cv2.imencode('.jpg', frame2, encode_param)
                #data = numpy.array(img_encode1)
                #stringData = data.tostring()
                #print (stringData)
                
                #rawait websocket.send(str(stringData))
                
#            elif ard1 == "2 open":
#                ardRes2.write('2 open'.encode())
#                print("box 2 open")
#                ardRes2 = box2.readline().decode('utf-8')
#                
#            elif '2 close' in ardRes2:
#                await websocet.send(ardRes2)
#                
#            if ard2 == "2 cam":
#                ret2, frame2 = capture2.read()
#                result, img_encode1 = cv2.imencode('.jpg', frame1, encode_param)
#                data = numpy.array(frame2)
#                stringData = base64.b64encode(data)
#                
#                print(stringData)
#
async def main():
    async with websockets.connect("wss://www.share42-together.com:8088/ws/locker", max_size=2048576) as websocket:
        task1 = asyncio.create_task(serial_task(websocket))
        task2 = asyncio.create_task(websocket_task(websocket))            
            
        asyncio.gather(task1, task2)

        
asyncio.run(main())

