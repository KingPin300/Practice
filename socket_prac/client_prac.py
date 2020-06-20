import socket


HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
DISCONNECT_MESSAGE = "EXIT"

SERVER = "192.168.1.39"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	message_length = len(message)
	send_length = str(message_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

send("Hello World!")
msg_length = client.recv(HEADER).decode(FORMAT)
if msg_length:
	msg_length = int(msg_length)
	msg = client.recv(msg_length).decode(FORMAT)
	print(f"[SERVER] {msg}")
send(DISCONNECT_MESSAGE)