import math

def signum(x):
  if x == 0:
    return 0
  
  elif x > 0:
    return 1
  
  else:
    return -1


def bisection(f, a, b, tol, N):
  if signum(f(a)) * signum(f(b)) > 0:
    print ("Initial conditions are not satisfied.")
    exit(0)
  """ Implements the bisection method.

  Args:
    f: The function to be bisected.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    tol: The tolerance.
    N: The maximum number of iterations.

  Returns:
    The root of the function or an error message.
  """

  i = 0
  while i < N:
    c = (a + b) / 2
    if signum(f(c)) == 0 or abs(b - a) <= tol:
      return c
    elif signum(f(a)) * signum(f(c)) < 0:
      b = c
    else:
      a = c
    i += 1
  print("Method Failure!")
  exit(0)


if __name__ == "__main__":
  f = lambda x: x**4 -x**3 + x**2 - 2
  a = 1
  b = 2
  tol = 1e-6
  N = 100
  a = 0

  root = bisection(f, a, b, tol, N)

  print("The approximate root of the function is", root, "and the value of the function at this point is ", f(root))
