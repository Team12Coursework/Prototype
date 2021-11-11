import socket
import threading

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 69500
address = (host,port)

socks.bind(address)
socks.listen()
print("hello world")