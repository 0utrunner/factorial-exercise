import functools # allows higher order functions(functions that act on or return other functions)
import operator # allows usage of operator functions

def factorial(num):
	numbers = []
	for i in range(num):
		numbers.append(i + 1)
		
	return(functools.reduce(operator.mul, numbers))
	
