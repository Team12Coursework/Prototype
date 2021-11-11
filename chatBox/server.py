import socket
import threading
import select

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 69500
server_address = (host,port)

socks.bind(server_address)
listening = socks.listen()

clients = ()

def serverListen() :
    while listening == True:
        connection, client_address = socks.accept()
        thread1 = threading.Thread(target=clientHandler, args=(connection, client_address))


def clientHandler(connection, client_address):
    pass
