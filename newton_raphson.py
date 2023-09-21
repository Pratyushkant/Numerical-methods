import math

def newton_raphson (f, p0, tol, N):
  i = 1
  while i <= N:
    if df(p0) == 0:
      print("Method Failure: Derivative at approximation vanished. The initial approximation is not close enough.")
      exit(0)
    else:
      p = p0 - f(p0)/df(p0)
      if abs(p0 - p) < tol:
        return p0
      else:
        p0 = p
        i = i + 1

    if i > N:
        print("Method Failure: Maximum number of iterations exceeded!")    
        exit(0)

if __name__ == "__main__":
  f = lambda x: math.cos(x) - x
  df = lambda x: - math.sin(x) - 1
  tol = 1e-6
  N = 100
  p0 = 1.5

  root = newton_raphson(f, p0, tol, N)

  print("The root of the function is", root, "and the value of the function at this point is approximately ", f(root))
