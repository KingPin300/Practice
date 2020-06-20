import socket
import threading


PORT = 5050
SERVER = "192.168.1.39" # my mothership ip
DISCONNECT_MESSAGE = "EXIT"
HEADER = 64
FORMAT = 'utf-8'


SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(connection, addr):
	print(f"[SERVER] {addr} connected.")
	connected = True
	while connected:
		msg_length = connection.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = connection.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False
			else:
				print(f"[{addr}] {msg}")
	print(f"[{addr}] has left the server.")
	connection.close()


def start():
	server.listen()
	while True:
		connection, addr = server.accept()
		myThread = threading.Thread(target=handleClient, args=(connection, addr))
		myThread.start()
		clients.append(myThread)
		print(f"[SERVER] active thread count {threading.activeCount() - 1 }.")


print(f"[SERVER] starting up on {ADDR[0]} port {ADDR[1]}.")
start()