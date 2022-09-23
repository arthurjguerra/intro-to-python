#Problem 2
#This module sums, subtratcs, multiplies, and divides two given integers. Arguments: (A and B).
#This module also prints the result. Arguments:(A, B, operation sign (string), operation result). 


#Print result fuction 
def show_result(A,B,sign,x):
    print('The result of ' + str(A) + sign + str(B) + ' is ' + str(x) + '.')
    
# Sum function
def sum_method(A,B):
    C = A + B
    return C
    
# Subtract function
def subtract_method(A,B):
    C = A - B
    return C

# Multiply function
def multiply_method(A,B):
    C = A * B
    return C

#Divide function
def divide_method(A,B):
    C = A / B
    return C

