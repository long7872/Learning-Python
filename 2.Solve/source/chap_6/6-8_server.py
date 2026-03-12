from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n**2

HOST = '127.0.0.1'
PORT = 8000
server = SimpleXMLRPCServer((HOST, PORT))
print("Listen to the signal from the port 8000...")
server.register_function(is_even)
server.serve_forever()