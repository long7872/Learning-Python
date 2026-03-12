import socket as sk

HOST = '127.0.0.1'
PORT = 1400
socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(2)
print("Server is ready !!!")
while 1:
    conn, addr = socket.accept()
    received_from_client = conn.recv(1024)
    print("Message of client:",received_from_client.decode())
    message = input("Enter message to send client: ")
    conn.send(message.encode())
    x = input("Shutdown Server? (y/n): ")
    if x == 'y':
        conn.close()
        break