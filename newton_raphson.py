import math

def f(x):
	return math.cos(x) - x

def df(x):
	return -math.sin(x) - 1

def newton_raphson(N, TOL, p):
	i = 1
	while i <= N:
		if (df(p) == 0):
			print ("Method Failure. Derivative became zero!")
			exit (0)
		newp = p - f(p)/df(p) 
		if abs(newp - p) < TOL:
			print ("The approximate root of the function is ", newp, " and the approximate value of the function at this point is ", f(newp))
			print ("Number of iterations taken are: ", i)
			exit(0)
		else:
			p = newp
			i = i + 1
	
	print ("Method Failure: Maximum number of iterations exceeded!")
	exit(0)

N = int(input("Enter the maximum number of iterations: "))
if N <= 0:
	print ("Invalid Input")
	exit(0)

TOL = float(input("Enter your tolerance: "))
if TOL <= 0:
	print ("Invalid Input")
	exit(0)

p = float(input("Enter your initial approximation (A word of caution: Newton's method works the best when the derivative at initial approximation is bounded away from zero!): "))
if (df(p) == 0):
	print ("Method Failure: Derivative at p is zero!")

newton_raphson (N, TOL, p)
