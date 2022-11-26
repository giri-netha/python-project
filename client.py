import socket

HOST = '10.0.2.184'

PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))

socket.send("HEllo World").encode('utf-8')

print(socket.recv(1024))
