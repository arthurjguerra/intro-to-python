#Problem 4
#This class sums, subtratcs, multiplies, and divides two given integers. Arguments: (A and B).
#This module also prints the result. Arguments:(A, B, operation sign (string), operation result). 

class Calculator:

	def __init__(self, A, B):
		self.A = A
		self.B = B
		

	#Print result fuction 
	def show_result(self, sign, x):
	    print('The result of ' + str(self.A) + sign + str(self.B) + ' is ' + str(x) + '.')
	    
	# Sum function
	def sum_method(self):
	    C = self.A + self.B
	    return C
	    
	# Subtract function
	def subtract_method(self):
	    C = self.A - self.B
	    return C

	# Multiply function
	def multiply_method(self):
	    C = self.A * self.B
	    return C

	#Divide function
	def divide_method(self):
	    C = self.A / self.B
	    return C

class SciCalculator:
	pass
