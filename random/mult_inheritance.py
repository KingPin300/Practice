"""
	multiple inheritance practice.
"""

class Mario():
	"""
		The Mario class has the move method.
	"""
	def move(self):
		"""
			The move method prints a specific message.
		"""
		print("I'm moving.")

class Shroom():
	"""
		The Shroom class has a eat_shroom method.
	"""
	def eat_shroom(self):
		"""
			The eat_shroom method prints a specific message.
		"""
		print("Eating a shroom!")

class Big_mario(Mario, Shroom):
	"""
		The Big_mario class inherits from both Mario and Shrrom classes for the
		methods: move and eat_shroom.
	"""
	pass

bigMario = Big_mario() # Big_mario methods.
print("A Big mario.")
bigMario.move()
bigMario.eat_shroom()

shroom = Shroom() # Shroom methods.
print("\nA Shroom.")
shroom.eat_shroom()

mario = Mario() # Mario methods.
print("\nA Mario.")
mario.move()