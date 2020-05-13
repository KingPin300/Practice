"""
	Classes and object practice program.
"""

class Enemy:
	"""
		The Enemy class show how we can create our own classes. Within the
		class there's variable within the class scope called life. An Enemy
		has three methods: attack, checkLife, heal.
	"""
	life = 3

	def attack(self):
		"""
			The attack method lets the enemy object to take damage, a hard
			hard coded 1 damage.
		"""
		print("ouch!")
		self.life -= 1

	def checkLife(self):
		"""
			The checkLife method give the enemy object the ability to tell us
			it's health or if it's dead.
		"""
		if self.life <= 0:
			print("I'm died!...")
			return 0
		else:
			print(f"I've got {self.life} left.")
			return 1

	def heal(self,points = 1):
		"""
			The heal mothed let's the enemy heal for x, or if nothing passed 1,
			and tells us how much it's healed too.
		"""
		self.life += points
		print(f"I'm being heal to {self.life}.")

enemy1 = Enemy() # creation of a enemy object.

while True: # calling attack on the enemy until he/she's dead.
	enemy1.attack()
	if enemy1.checkLife() == 0:
		break
enemy1.heal()