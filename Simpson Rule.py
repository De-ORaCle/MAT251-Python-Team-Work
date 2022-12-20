import math

# Define the function to integrate
def f(x):
    return x**2 + 3*x + 2

# Collect inputs from the user
a_str = input("Enter the lower bound of the integral: ")
b_str = input("Enter the upper bound of the integral: ")
n_str = input("Enter the number of intervals to use in the approximation: ")

# Convert the inputs from strings to floats
a = float(a_str)
b = float(b_str)
n = int(n_str)

# Calculate the step size for Simpson's rule
step = (b - a) / n

# Initialize the sum to 0
sum = 0

# Iterate over the intervals and sum the areas of the trapezoids
for i in range(n):
    # Calculate the lower and upper bounds of the interval
    x_lower = a + i * step
    x_upper = a + (i + 1) * step
    
    # Calculate the value of the function at the lower and upper bounds
    y_lower = f(x_lower)
    y_upper = f(x_upper)
    
    # Calculate the value of the function at the midpoint of the interval
    x_mid = (x_lower + x_upper) / 2
    y_mid = f(x_mid)
    
    # Calculate the area of the trapezoid using Simpson's rule and add it to the sum
    area = (y_lower + 4*y_mid + y_upper) * step / 3
    sum += area

# The integral is the sum of the areas of the trapezoids
I = sum

# Print the result
print("The approximate integral of the function is:", I)
