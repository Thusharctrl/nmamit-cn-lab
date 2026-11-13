#server
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8888))
s.listen(1)

print("Server is listening for incoming connections...")

while True:
    c, addr = s.accept()
    print("Accepted connection from", addr)

    name = c.recv(1024).decode()
    print("Received file name:", name)

    if os.path.exists(name):
        f = open(name, "rb")
        data = f.read()
        f.close()
        c.send(data)
    else:
        c.send(b"File not found")

    c.close()




#tcp_client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8888))

name = input("Enter the file name: ")
s.send(name.encode())

data = s.recv(1024).decode()

if data == "File not found":
    print("File not found on server")
else:
    print("File contents:")
    print(data)

s.close()
