from Module import Calculator

x = 6
y = 3

calc = Calculator(x, y)


result_sum = calc.sum_method()
calc.show_result('+',result_sum)

result_sub = calc.subtract_method()
calc.show_result('-',result_sub)

result_mult = calc.multiply_method()
calc.show_result('*',result_mult)

result_div = calc.divide_method()
calc.show_result('/',result_div)




