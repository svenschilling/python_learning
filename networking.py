import socket as sock

mySocket = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
mySocket.connect(('google.de',80))
print(mySocket)