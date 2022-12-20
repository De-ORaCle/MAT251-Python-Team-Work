def trapezoidal(f, a, b):
  return (b - a) * (f(a) + f(b)) / 2

'''
This function takes a function f and the limits of integration a and b, and returns the approximate value of the definite integral of f over the interval [a, b].

To use this function, you can call it with the desired function and limits of integration as arguments. For example:
'''

def f(x):
  return x**2

result = trapezoidal(f, 0, 1)
print(result)

#This would approximate the integral of f(x) = x**2 from 0 to 1, and print the result.
