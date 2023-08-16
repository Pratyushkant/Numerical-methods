def f(x):
	return (x**2 -1)/3

def fixed_point_iteration (TOL, N_0, p_0):
	i = 1
	while i <= N_0:
		p = f(p_0)
		if abs(p - p_0) < TOL:
			print("The fixed point approximated is: ", p)
			exit(0)
		else:
			i += 1
			p_0 = p

	

p_0 = float(input("Enter the initial approximation: "))
N_0 = int(input("Enter the maximum number of iterations: "))
if N_0 <= 0:
	exit(0)
	
TOL = float(input("Enter the tolerance: "))
fixed_point_iteration(TOL, N_0, p_0)
print("Method faliure :(")
