import socket
import threading

PORT = 5050
SERVERIP = "192.168.1.39" # my mothership ip
DISCONNECT_MESSAGE = "EXIT"
HEADER = 64
FORMAT = 'utf-8'