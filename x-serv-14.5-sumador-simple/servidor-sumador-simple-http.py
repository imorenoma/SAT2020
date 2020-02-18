#!/usr/bin/python3

import socket
import random
import calculadora


Port = 1234


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Establish Connection with sockets

mySocket.bind((socket.gethostname(), Port))
mySocket.listen(20)     # Maximum connection allowed 20

try:
    while True:

        print("Waiting for connections")
        (recvSocket, address) = mySocket.accept()
        print("Request Received")

        request = str(recvSocket.recv(2048), 'utf-8')
        print(request)

        resource = request.split()[1]

        _, operacion, num1, num2 = resource.split('/')

        number1 = int(num1)
        number2 = int(num2)

        html_response = calculadora.operation[operacion](number1,number2)

        recvSocket.send(bytes("HTTP/1.1 200 ok\r\n\r\n " +
                              '<html><h2>Sumador Simple</h2>' +
                              str(html_response) +
                              '\r\n', 'utf-8'))

        recvSocket.close()
except KeyboardInterrupt:
    print("Closing Connection")
    mySocket.close()
