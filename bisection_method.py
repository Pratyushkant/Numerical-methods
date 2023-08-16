def bisection(f, a, b, tol, N):
  """Implements the bisection method.

  Args:
    f: The function to be bisected.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    tol: The tolerance.
    N: The maximum number of iterations.

  Returns:
    The root of the function.
  """

  i = 0
  while abs(b - a) > tol and i < N:
    c = (a + b) / 2
    if f(c) == 0:
      return c
    elif f(a) * f(c) < 0:
      b = c
    else:
      a = c
    i += 1
  return (a + b) / 2


if __name__ == "__main__":
  f = lambda x: x**4 -x**3 + x**2 - 2
  a = 0
  b = 2
  tol = 1e-6
  N = 100

  root = bisection(f, a, b, tol, N)

  print("The root of the function is", root)