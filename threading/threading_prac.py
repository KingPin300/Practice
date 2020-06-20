"""
	Basic threading practice.
"""
import threading

class Messenger(threading.Thread):
	"""
		The Messager class that inherits from the thread class.
	"""
	def run(self):
		"""
			The run method, from threading, prints out the threads name 10 times.
		"""
		for _ in range(10):
			print(threading.current_thread().getName())

# Create two messengers.
thread1 = Messenger(name = 'thread1')
thread2 = Messenger(name = 'thread2')

# Start the messengers. Key step to getting the threads to work.
thread1.start()
thread2.start()