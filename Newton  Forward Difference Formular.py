# define the function to compute the forward difference
def newton_forward_difference(x, y, h):
  n = len(x)
  f = [[0 for i in range(n)] for j in range(n)]
  
  # store the y values in the first column of the table
  for i in range(n):
    f[i][0] = y[i]
  
  # compute the rest of the table using the forward difference formula
  for j in range(1, n):
    for i in range(n - j):
      f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])
  
  return f

# define the function to compute the value of the polynomial at a given point
def eval_newton_forward_difference(x, a, h):
  n = len(x)
  p = a[n-1]
  
  for i in range(n-2, -1, -1):
    p = p * (h - x[i]) + a[i]
  
  return p

'''
The newton_forward_difference function computes the table of forward differences using the input arrays x and y, which are the points at which the function is evaluated, and the value h at which the polynomial will be evaluated.

The eval_newton_forward_difference function uses the table of forward differences and the input arrays x and h to evaluate the polynomial at the point h.

You can collect input from the user by using the input() function. For example:
'''

# collect input from the user
x_input = input("Enter the x values separated by commas: ")
y_input = input("Enter the y values separated by commas: ")
h_input = input("Enter the value at which to evaluate the polynomial: ")

# split the input strings into lists of values
x = [float(x) for x in x_input.split(",")]
y = [float(y) for y in y_input.split(",")]
h = float(h_input)

# compute the table of forward differences
table = newton_forward_difference(x, y, h)

# compute the value of the polynomial at the point h
result = eval_newton_forward_difference(x, table[0], h)

print(result)
