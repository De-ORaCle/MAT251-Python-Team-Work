def rectangular_rule(f, a, b, n):
    # Calculate the width of each subinterval
    h = (b - a) / n

    # Calculate the midpoints of the subintervals
    midpoints = [a + h * (i + 0.5) for i in range(n)]

    # Calculate the sum of the areas of the rectangles
    sum_areas = sum(f(x) * h for x in midpoints)

    return sum_areas


# Define the function to be integrated
def f(x):
    return x ** 2


# Collect input from the user
a = float(input("Enter the lower bound of the interval: "))
b = float(input("Enter the upper bound of the interval: "))
n = int(input("Enter the number of subintervals: "))

# Approximate the definite integral using the rectangular rule
result = rectangular_rule(f, a, b, n)

# Print the result
print(f"The approximate value of the integral is: {result}")
