#Problem 2
#This module sums, subtratcs, multiplies, and divides two given integers.
# It is called with hard-coded values. 

#Print result fuction (to be updated ***)
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

# It is printed in the hard-code way (to be improved ***)

x = 6
y = 3

result1 = sum_method(x,y)
show_result(x,y,'+',result1)

result2 = subtract_method(x,y)
show_result(x,y,'-',result2)

result3 = multiply_method(x,y)
show_result(x,y,'*',result3)

result4 = divide_method(x,y)
show_result(x,y,'/',result4)
