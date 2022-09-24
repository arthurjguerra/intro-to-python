from Module import Calculator

calc = Calculator()

x = 6
y = 3

result_sum = calc.sum_method(x,y)
calc.show_result(x,y,'+',result_sum)

result_sub = calc.subtract_method(x,y)
calc.show_result(x,y,'-',result_sub)

result_mult = calc.multiply_method(x,y)
calc.show_result(x,y,'*',result_mult)

result_div = calc.divide_method(x,y)
calc.show_result(x,y,'/',result_div)




