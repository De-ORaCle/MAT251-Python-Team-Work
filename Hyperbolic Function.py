import math

# Collect input from the user
x_str = input("Enter the value of x: ")

# Convert the input from a string to a float
x = float(x_str)

# Calculate the values of sinh, cosh, and tanh
sinh_x = (math.exp(x) - math.exp(-x)) / 2
cosh_x = (math.exp(x) + math.exp(-x)) / 2
tanh_x = sinh_x / cosh_x

# Print the results
print("sinh(x) =", sinh_x)
print("cosh(x) =", cosh_x)
print("tanh(x) =", tanh_x)
