import socket as sk

HOST = '127.0.0.1'
PORT = 1400
socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket.connect((HOST,PORT))
while 1:
    message = input("Client 2 send a message to server: ")
    socket.send(message.encode())
    data_from_server = socket.recv(1024)
    print("Message of Server sending:",data_from_server.decode())
    x = input("Shutdown Client? (y/n): ")
    if x == 'y':
        socket.close()
        break