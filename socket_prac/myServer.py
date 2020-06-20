from myInfoTable import *

clients = {}

class MyServer(threading.Thread):
	def __init__(self, port, *args, **kwargs):
		super(MyServer, self).__init__(*args, **kwargs)
		self.ADDR = (socket.gethostbyname(socket.gethostname()), port)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.ADDR)

	def run(self, *args, **kwargs):
		super(MyServer, self).run(*args,**kwargs)
		consoleListenerThread = threading.Thread(
			target = MyServer. consoleListener)
		consoleListenerThread.start()
		self.clientListener()

	def clientListener(self):
		self.server.listen()
		while True:
			connection, addr = self.server.accept()
			newThread = threading.Thread(target = MyServer.handleClient, args=(self, connection, addr))
			newThread.start()
			clients.update({addr[1]:(newThread,connection)})

	def handleClient(self, connection, addr):
		print(f"[SERVER] {addr} connected.")
		connected = True
		print(f"number of clients: {len(clients)}")
		while connected:
			msg_length = connection.recv(HEADER).decode(FORMAT)
			if msg_length:
				msg_length = int(msg_length)
				msg = connection.recv(msg_length).decode(FORMAT)
				if msg == DISCONNECT_MESSAGE:
					connected = False
				else:
					print(f"[{addr}] {msg}")
					MyServer.send(connection, "thank you!")

		print(f"[{addr}] has left the server.")
		clients.pop(addr[1])
		connection.close()

	def send(client, msg):
		message = msg.encode(FORMAT)
		message_length = len(message)
		send_length = str(message_length).encode(FORMAT)
		send_length += b' ' * (HEADER - len(send_length))
		client.send(send_length)
		client.send(message)

	def consoleListener():
		print("console...")
		while True:
			msg = str(input())
			for client in clients:
				message = msg.encode(FORMAT)
				message_length = len(message)
				send_length = str(message_length).encode(FORMAT)
				send_length += b' ' * (HEADER - len(send_length))
				clients[client][1].send(send_length)
				clients[client][1].send(message)

server = MyServer(port = PORT, name = "SERVER")
server.start()
server.join()