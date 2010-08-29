import sys
import math

class Person():
	name = ""
	income = 0.0
	due = 0.0
	
	def __init__(self,name='A Person',income=0.0):
		self.name = name
		self.income = float(income)

class Calculator():
	people = []
	charge = 0.0
	total_income = 0.0
	
	def calculate(self):
		self.total_income = 0.0
		
		for i in self.people:
			self.total_income += i.income
		
		for i in self.people:
			this_inc = i.income
			ratio = this_inc/self.total_income
			due = self.charge*ratio
			
			# We always want to round up, there is no proper float rounding in 
			# python so we times it by 100, then round it, then divide it again.
			due *= 100
			due = math.ceil(due)
			due /= 100
			
			i.due = due

def main(argv=None):
	people = [
		Person("Person 1",500),
		Person("Person 2",1000),
		Person("Person 3",1500),
	]
	
	calc = Calculator()
	calc.people = people
	calc.charge = 42.95
	calc.calculate()
	
	print "UDE Bill Calculator"
	print "Total income including all parties: ${0:03.2f}".format(calc.total_income)
	
	for p in calc.people:
		print "Amount due by {0} is ${1:03.2f}".format(p.name,p.due)ue

if __name__ == "__main__":
	sys.exit(main())
























































