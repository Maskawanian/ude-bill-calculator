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
	due_sum = 0.0
	due_percent = 0.0
	
	def calculate(self):
		self.total_income = 0.0
		self.due_sum = 0.0
		
		for i in self.people:
			self.total_income += i.income
		
		for i in self.people:
			this_inc = i.income
			ratio = this_inc/self.total_income
			due = self.charge*ratio
			
			self.due_percent = (math.ceil((due/this_inc)*10000))/100
			
			# We always want to round up, there is no proper float rounding in 
			# python so we times it by 100, then round it, then divide it again.
			due *= 100
			due = math.ceil(due)
			due /= 100
			
			i.due = due
			self.due_sum += due
