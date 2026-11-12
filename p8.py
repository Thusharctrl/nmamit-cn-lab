#tcp_server.py

import socket
import os

HOST = "127.0.0.1"
PORT = 8888
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening on", HOST, "port", PORT)

try:
    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print("Accepted connection from", client_address)
            file_name = client_socket.recv(BUFFER_SIZE).decode()
            print("Received file name =", file_name)
            if os.path.isfile(file_name):
                with open(file_name, "rb") as file:
                    client_socket.sendall(file.read())
                print("File sent")
            else:
                client_socket.sendall(b"File not found")
                print("File not found")
except KeyboardInterrupt:
    print("\nServer stopped")
finally:
    server_socket.close()




#tcp_client.py

import socket
import sys
import os

SERVER_ADDRESS = ("127.0.0.1", 8888)
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(SERVER_ADDRESS)
except ConnectionRefusedError:
    sys.exit("Could not connect to the server. Is tcp_server.py running?")

file_name = input("Enter the file name: ").strip()
if file_name == "":
    client_socket.close()
    sys.exit("No file name entered.")

client_socket.sendall(file_name.encode())
file_contents = b""
while True:
    chunk = client_socket.recv(BUFFER_SIZE)
    if not chunk:
        break
    file_contents += chunk
client_socket.close()

if file_contents == b"File not found":
    print("File not found on the server.")
else:
    print("File contents:")
    print(file_contents.decode(errors="replace"))
    save_name = "received_" + os.path.basename(file_name)
    with open(save_name, "wb") as file:
        file.write(file_contents)
    print("File received and saved as '" + save_name + "'")
