class Person:
	def __init__(self, number_of_arms, height, weight, number_of_fingers, name):
		self.number_of_arms=number_of_arms
		self.height=height
		self.weight=weight
		self.number_of_fingers=number_of_fingers
		self.name=name
	def printHeight(self):
		return self.name,"is",self.height,"inches tall."
	def printArms(self):
		return Jacob.name,"has",Jacob.number_of_arms,"arms."


Jacob=Person(2, 55, 72, 10, "Jacob")
print Jacob.name,"is",Jacob.height,"inches tall."
print Jacob.printHeight()
print Jacob.printArms()
# print Jacob.name,"has",Jacob.number_of_arms,"arms."

