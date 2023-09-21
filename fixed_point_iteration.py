import math

def fixed_point (f, p0, tol, N):
  i = 1
  while i <= N:
    p = f(p0)
    if abs(p0 - f(p0)) < tol:
      return p0
    else:
      p0 = f(p0)
      i = i + 1

    if i > N:
        print("Method Failure: Maximum number of iterations exceeded!")    
        exit(0)

if __name__ == "__main__":
  f = lambda x: (x**2 - 1) / 3
  tol = 1e-6
  N = 100
  p0 = 0

  fixed_point = fixed_point(f, p0, tol, N)

  print("The fixed point of the function is", fixed_point, "and the value of the function at this point is ", f(fixed_point))
