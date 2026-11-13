#server
import socket
import os

serverAddress = ("localhost", 8888)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(serverAddress)

serverSocket.listen(1)

print("Server is listening for incoming connections...")

while True:
    clientSocket, clientAddress = serverSocket.accept()

    print("Accepted connection from", clientAddress)

    fileName = clientSocket.recv(1024).decode()

    print("Received file name:", fileName)

    if os.path.exists(fileName):
        file = open(fileName, "rb")
        fileContents = file.read()
        file.close()

        clientSocket.send(fileContents)

    else:
        clientSocket.send(b"File not found")

    clientSocket.close()



#tcp_client.py
import socket

serverAddress = ("localhost", 8888)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(serverAddress)

fileName = input("Enter the file name: ")

clientSocket.send(fileName.encode())

fileContents = clientSocket.recv(1024).decode()

if fileContents == "File not found":
    print("File not found on server")
else:
    print("File contents:")
    print(fileContents)

clientSocket.close()
