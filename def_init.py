"""
	Use of __init__ method within a class Enemy.
"""

class Enemy:
	"""
		The Enemy class show how we can create our own classes with an init.
		An Enemy has an init and a method called get_hp.
	"""

	def __init__(self, hp, name):
		"""
			The __init__ method gives the name and hp to the enemy.
		"""
		self.hp = hp
		self.name = name
		print(f"{self.name} has been made.")

	def get_hp(self):
		"""
			The get_hp method shows the name and the hp of the enemy.
		"""
		print(f"{self.name}s HP is {self.hp}.")

# create two enemy.
# look at their hps.
toad = Enemy(5, "Toad")
toad.get_hp()
cat = Enemy(10, "Cat")
cat.get_hp()