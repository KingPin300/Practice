from myInfoTable import *
import time

class MyClient(threading.Thread):
	def __init__(self, port, ip, *args, **kwargs):
		super(MyClient, self).__init__(*args, **kwargs)
		self.ADDR = (ip, port)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.ADDR)

	def run(self, *args, **kwargs):
		super(MyClient, self).run(*args, **kwargs)
		MyClient.send(self, "Hello World!")
		MyClient.recieve(self)

	def send(self, msg):
		message = msg.encode(FORMAT)
		message_length = len(message)
		send_length = str(message_length).encode(FORMAT)
		send_length += b' ' * (HEADER - len(send_length))
		self.client.send(send_length)
		self.client.send(message)

	def recieve(self):
		msg_length = self.client.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = self.client.recv(msg_length).decode(FORMAT)
			print(f"[SERVER] {msg}")
		MyClient.send(self, DISCONNECT_MESSAGE)

myClient = MyClient(port = PORT, ip = SERVERIP, name = "CLIENT")
myClient.start()
time.sleep(15)
myClient.join()