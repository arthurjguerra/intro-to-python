#Problem 4
#This class sums, subtratcs, multiplies, and divides two given integers. Arguments: (A and B).
#This module also prints the result. Arguments:(A, B, operation sign (string), operation result). 

class Calculator:

	#Print result fuction 
	def show_result(self,A,B,sign,x):
	    print('The result of ' + str(A) + sign + str(B) + ' is ' + str(x) + '.')
	    
	# Sum function
	def sum_method(self,A,B):
	    C = A + B
	    return C
	    
	# Subtract function
	def subtract_method(self,A,B):
	    C = A - B
	    return C

	# Multiply function
	def multiply_method(self,A,B):
	    C = A * B
	    return C

	#Divide function
	def divide_method(self,A,B):
	    C = A / B
	    return C

class SciCalculator:
	pass
