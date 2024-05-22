import json
import random
from socket import *
import time
from gpiozero import MotionSensor
from signal import pause
import datetime

pir = MotionSensor(25)

serverName = '255.255.255.255'
serverPort = 10101
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
keep_communicating = True

# def speed_generator():
#     sensor_name = "Mettes speedtrap"
#     speed = random.randint(60, 100)
#     speed_json = json.dumps({"SensorName": sensor_name, "Speed": speed})
#     clientSocket.sendto(speed_json.encode(), (serverName, serverPort))
#     return speed_json

def motion_detector():
    if(pir.motion_detected):
        motion_data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        motion_json = json.dumps({"activeMotion": motion_data})
        clientSocket.sendto(motion_json.encode(), (serverName, serverPort))
        return motion_json


while keep_communicating:
    motion_data = motion_detector()
    print(motion_data)
    time.sleep(1)

clientSocket.close()