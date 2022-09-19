#Problem 2
#This module sums, subtratcs, multiplies, and divides two given integers.
# It is called with hard-coded values. 

# Declare two integers, variables A and B
A = 6
B = 3

#Print result fuction (to be updated ***)
def show_result(sign,x):
    pass

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

# It is printed in the hard-code way (to be improved ***)
result1 = sum_method(A,B)
print('The result of ' + str(A) + ' + ' + str(B) + ' is ' + str(result1) + '.')

result2 = subtract_method(A,B)
print('The result of ' + str(A) + ' - ' + str(B) + ' is ' + str(result2) + '.')

result3 = multiply_method(A,B)
print('The result of ' + str(A) + ' * ' + str(B) + ' is ' + str(result3) + '.')

result4 = divide_method(A,B)
print('The result of ' + str(A) + ' / ' + str(B) + ' is ' + str(result4) + '.')
