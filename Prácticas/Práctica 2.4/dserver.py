import socket
import time
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.43.96.116', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
cosas = []

def sendmessage(ip,mensaje):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, 8089)) #yorch
    clientsocket.send(mensaje)
    clientsocket.close()
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        cosas.append(buf)
        print(cosas)
        if(buf=='plox'):
            time.sleep(2)

            sendmessage('10.43.51.252',cosas[0])
            sendmessage('10.43.51.252',cosas[1])
