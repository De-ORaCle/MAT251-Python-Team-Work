def runge_kutta(f, x0, y0, x_final, h):
  # Initialize the solution array
  x = [x0]
  y = [y0]
  
  # Loop until we reach the final value of x
  while x[-1] < x_final:
    # Compute the next value of x and y using the Runge-Kutta method
    k1 = h * f(x[-1], y[-1])
    k2 = h * f(x[-1] + h/2, y[-1] + k1/2)
    k3 = h * f(x[-1] + h/2, y[-1] + k2/2)
    k4 = h * f(x[-1] + h, y[-1] + k3)
    x_next = x[-1] + h
    y_next = y[-1] + (k1 + 2*k2 + 2*k3 + k4)/6
    
    # Add the new x and y values to the solution arrays
    x.append(x_next)
    y.append(y_next)
  
  return x, y

# Prompt the user for the initial values of x and y
x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))

# Prompt the user for the final value of x and the step size h
x_final = float(input("Enter the final value of x: "))
h = float(input("Enter the step size h: "))

# Prompt the user for the function f(x,y)
f_string = input("Enter the function f(x,y) as a Python expression: ")

# Convert the string to a function
f = lambda x, y: eval(f_string)

# Solve the ODE using the Runge-Kutta method
x, y = runge_kutta(f, x0, y0, x_final, h)

# Print the solution
print("x =", x)
print("y =", y)

'''
This code defines a function runge_kutta that takes as input a function f(x, y) representing the ODE, the initial values of x and y, the final value of x, and the step size h. It uses the Runge-Kutta method to compute a sequence of values x and y that approximate the solution to the ODE.

The code then prompts the user for the initial values of x and y, the final value of x, the step size h, and the function f(x, y). It converts the function f(x, y) from a string input by the user into a lambda function and calls the runge_kutta function to solve the ODE. Finally, it prints the solution.
'''