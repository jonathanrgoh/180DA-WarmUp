import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('DESKTOP-C5T6AL1', 1234))
client.send("I am CLIENT\n")
from_server = client.recv(4096)
client.close()
print(from_server)