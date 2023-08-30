import math

def f(x):
	return math.cos(x) - x

def secant_method(N, TOL, p1, p2):
	i = 1
	while i <= N:
		q1 = f(p1)
		q2 = f(p2)
		p = p2 - q2*(p2 - p1)/(q2 - q1)
		
		if (p1 == p2):
			print ("Method Failure. Secant cannot be formed.")
			exit (0)
			
		if abs(p - p2) < TOL:
			print ("The approximate root of the function is ", p, " and the approximate value of the function at this point is ", f(p))
			print ("Number of iterations taken are: ", i)
			exit(0)
			
		else:
			p1 = p2
			p2 = p
			q1 = q2
			q2 = f(p)
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

p1 = float(input("Enter your first initial approximation: "))

p2 = float(input("Enter your second initial approximation: "))


secant_method (N, TOL, p1, p2)
