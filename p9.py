#server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 20001))

print("UDP server listening...")

while True:
    data, addr = s.recvfrom(1024)
    a, op, b = data.decode().split()

    a = float(a)
    b = float(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    elif op == "%":
        result = a % b

    print("Result:", result)
    s.sendto(str(result).encode(), addr)


#client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = input("Enter first number : ")
op = input("Enter operator (+ - * / %) : ")
b = input("Enter second number : ")

msg = a + " " + op + " " + b

s.sendto(msg.encode(), ("127.0.0.1", 20001))

data, addr = s.recvfrom(1024)

print(msg, "=", data.decode())

s.close()
