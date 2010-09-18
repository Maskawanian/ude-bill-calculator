import sys
import math
from Calculator import Person,Calculator

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
	
	print "Total income including all parties: ${0:03.2f}".format(calc.total_income)
	
	for p in calc.people:
		print "Amount due by {0} whose income is ${1:03.2f} is ${2:03.2f}.".format(p.name,p.income,p.due)
	
	print "Each party is paying ${0:03.2f}% of their income.".format(calc.due_percent)

if __name__ == "__main__":
	sys.exit(main())
























































