"""
	practice with inheritance.
"""

class Parent():
	"""
		The Parent class that has just a last name.
	"""

	def print_last_name(self):
		"""
			The print_last_name method prints the parents last name.
		"""
		print("Johnson")


	def print_first_name(self):
		"""
			The print_first_name method prints the parents first name.
		"""
		print("Ron")


class Child(Parent):
	"""
		The Child class that inherits it's last name from the parent.
		Takes uses of the print_last_name method.
	"""

	def print_first_name(self):
		"""
			The print_first_name method prints the childs first name.
			This overrides the method from Parent class.
		"""
		print("Damion")


kid = Child() # Testing the Child class.
print("Me:")
kid.print_first_name()
kid.print_last_name()
dad = Parent() # Testing the Parent class.
print("\nMy father:")
dad.print_first_name()
dad.print_last_name()