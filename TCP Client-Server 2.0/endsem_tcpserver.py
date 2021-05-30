import socket

def perfect_num(n):
	sum = 0
	for i in range(1,n):
		if n%i ==0:
			sum += i
	return str(sum == n)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 22000))
serversocket.listen()
connection, address = serversocket.accept()
print("Connection has been established")
msg = connection.recv(1024)
received=msg.decode()
number=int(received)
message=perfect_num(number)
connection.send(message.encode())
connection.close()
serversocket.close()
