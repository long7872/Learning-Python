import socket as sk
HOST = '127.0.0.1'
PORT = 1400
socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket.connect((HOST,PORT))
send = input("Hi, Server: ").encode()
socket.send(send)
data_from_server = socket.recv(1024)
print(data_from_server.decode())
socket.close()