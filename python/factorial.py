import functools
import operator

def factorial(num):
	numbers = []
	for i in range(num):
		numbers.append(i + 1)
		
	return(functools.reduce(operator.mul, numbers))
	
