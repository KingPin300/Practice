"""
	To run each test remove the triple quotes and then run. DON'T remove
	more than one group of triple quotes because it will crash.
"""

import threading
import time


print("main thread is starting...")



"""
	The use of multiple Threads.
"""
"""
threads_list = []

def func(name, sleepV):
	print(f'ran {name}.')
	time.sleep(sleepV)
	print(f'done {name}.')

for i in range(1, 10):
	x = threading.Thread(target=func, args=(str(i),i), name = f"thread{i}")
	threads_list.append(x)
	x.start()

for t in threads_list:
	t.join()

"""


"""
	The use of personal subclass of Threads, changing just run and
	leaving __init__ alone.
"""
"""
def func(name, sleepV):
	print(f'ran {name}.')
	time.sleep(sleepV)
	print(f'done {name}.')

class MyThread(threading.Thread):
	def run(self):
		print("start of personal thread class.")
		#
		try:
			if self._target:
				self._target(*self._args, **self._kwargs)
		finally:
			del self._target, self._args, self._kwargs
		#
		print("end of personal thread class.")

t = MyThread(target = func, args = ("Cat",5))
t.start()
t.join()
"""

"""
	The use of personal subclass of Threads, changing just __init__ but also
	having to changing run.
"""
"""
def func(name, sleepV):
	print(f'ran {name}.')
	time.sleep(sleepV)
	print(f'done {name}.')

class MyThread(threading.Thread):
	def __init__(self, number, func, args):
		threading.Thread.__init__(self)
		self.number = number
		self.func = func
		self.args = args

	def run(self):
		print(f"thread {self.number} has started.")
		self.func(*self.args)
		print(f"thread {self.number} has started.")

t = MyThread(5, func, ("Stan",5))
t.start()
t.join()
"""

"""
	The use of personal subclass of Threads, changing just __init__ but also
	having to changing run but using super to keep original functionality.
"""
"""
def func(name, sleepV):
	print(f'ran {name}.')
	time.sleep(sleepV)
	print(f'done {name}.')

class MyThread(threading.Thread):
	def __init__(self, name, sleepV, *args, **kwargs):
		super(MyThread, self).__init__(*args, **kwargs)
		self.name = name
		self.sleepV = sleepV

	def run(self, *args, **kwargs):
		print(f"thread {self.name} has started.")
		super(MyThread, self).run(*args,**kwargs)
		print(f"thread {self.name} has ended.")

t = MyThread(name = "Dad", sleepV = 5, target = func, args = ("DAD", 5))
t.start()
t.join()
"""

print("main thread is finished.")