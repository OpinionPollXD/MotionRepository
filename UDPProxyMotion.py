from socket import *

import requests

serverPort = 10101
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('', serverPort)

api_adress = "https://restopinionpoll.azurewebsites.net/api/Motions"
headersArray = {'Content-type': 'application/json'}  

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
     message, clientAddress = serverSocket.recvfrom(2048)
     print("Received message:" + message.decode())
     requests.post(api_adress, data=message, headers=headersArray)