#server
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 20001
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
print("UDP server up and listening on port", SERVER_PORT)

try:
    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        request = data.decode(errors="replace")
        print("Request from", client_address, ":", request)

        try:
            num1, operator, num2 = request.split()
            a = float(num1)
            b = float(num2)
            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    result = "Error: division by zero"
                else:
                    result = a / b
            elif operator == "%":
                if b == 0:
                    result = "Error: modulo by zero"
                else:
                    result = a % b
            else:
                result = "Error: invalid operator"
        except ValueError:
            result = "Error: invalid request"

        print("Result to client:", result)
        server_socket.sendto(str(result).encode(), client_address)
except KeyboardInterrupt:
    print("\nServer stopped")
finally:
    server_socket.close()


#client
import socket
import sys
import math

SERVER_ADDRESS = ("127.0.0.1", 20001)
BUFFER_SIZE = 1024

def is_number(text):
    try:
        return math.isfinite(float(text))
    except ValueError:
        return False

num1 = input("Enter first number : ").strip()
operator = input("Enter operator (+ - * / %) : ").strip()
num2 = input("Enter second number : ").strip()

if not is_number(num1) or not is_number(num2):
    sys.exit("Invalid input: both operands must be numbers.")
if operator not in ("+", "-", "*", "/", "%"):
    sys.exit("Invalid operator: use one of + - * / %")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

request = num1 + " " + operator + " " + num2
client_socket.sendto(request.encode(), SERVER_ADDRESS)

try:
    reply, server_address = client_socket.recvfrom(BUFFER_SIZE)
    print(request, "=", reply.decode())
except (socket.timeout, ConnectionResetError):
    print("No reply from the server. Is udp_server.py running?")
finally:
    client_socket.close()
