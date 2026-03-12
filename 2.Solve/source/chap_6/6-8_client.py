import xmlrpc.client

HOST = '127.0.0.1'
PORT = 8000
with xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}/") as proxy:
    print("Square a number ")
    a = int(input("Enter a positive interger: "))
    print("Square a number is:", str(proxy.is_even(a)))