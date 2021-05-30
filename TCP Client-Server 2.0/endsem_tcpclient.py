import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 22000))
message=input("Enter a number:")
clientsocket.send(message.encode())
msg = clientsocket.recv(1024)
received = msg.decode()
if "True" in received:
	print(message+" is a perfect number")
elif "False" in received:
	print(message+" is not a perfect number")
clientsocket.close()
