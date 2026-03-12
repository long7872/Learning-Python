import socket as sk
HOST = '127.0.0.1'
PORT = 1400
socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(1)
print("Wait from Client \n")
socket, add_client = socket.accept()
print('Connected to address:', add_client)
while 1:
    data_from_client = socket.recv(1024)
    if not data_from_client: break
    answer1 = 'Receive a Message from Client, That is: '.encode()
    answer2 = '. Good Bye, See you again'.encode()
    socket.send(answer1 + data_from_client + answer2)