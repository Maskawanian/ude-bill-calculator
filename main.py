import sys

class Income():
	name = ""
	amount = 0.0
	
	def __init__(self,name='bill name',amount=0.0):
		self.name = name
		self.amount = float(amount)




def main(argv=None):
	incomes = [
		Income("Person 1",500),
		Income("Person 2",1000),
		Income("Person 3",1500),
	]
	print "main"
	pass



if __name__ == "__main__":
	sys.exit(main())
