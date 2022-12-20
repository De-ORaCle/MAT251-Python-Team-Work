import math

def taylor_expansion(f, x, n):
    """Approximates the function f at the point x using the Taylor series expansion with n terms.
    
    Args:
        f: The function to approximate.
        x: The point at which to approximate the function.
        n: The number of terms in the Taylor series expansion.
    
    Returns:
        The approximation of the function f at the point x.
    """
    # Initialize the approximation to the first term of the Taylor series expansion
    approximation = f(x)
    
    # Loop through the remaining terms of the Taylor series expansion
    for i in range(1, n):
        # Compute the next term of the Taylor series expansion and add it to the approximation
        approximation += (f(x + i) - f(x)) / math.factorial(i)
    
    # Return the approximation
    return approximation

# Define the function to approximate
def f(x):
    return math.sin(x)

# Get the point at which to approximate the function from the user
x = float(input("Enter the point at which to approximate the function: "))

# Get the number of terms in the Taylor series expansion from the user
n = int(input("Enter the number of terms in the Taylor series expansion: "))

# Approximate the function at the given point using the Taylor series expansion with the specified number of terms
approximation = taylor_expansion(f, x, n)

# Print the approximation
print(f"The approximation of f({x}) is {approximation}.")


'''
This code defines a function called taylor_expansion that takes three arguments: a function f, a point x at which to approximate f, and an integer n specifying the number of terms in the Taylor series expansion. The function returns the approximation of f at x using the Taylor series expansion with n terms.

The function f to approximate and the point x at which to approximate it are both input by the user. The number of terms in the Taylor series expansion is also input by the user.

The taylor_expansion function computes the Taylor series expansion by looping through the terms of the expansion and adding each term to the approximation. The first term of the expansion is simply the value of the function at the point x. The remaining terms are computed using the formula for the nth term of the Taylor series expansion:

(f(x + i) - f(x)) / i!

where i is the index of the term in the expansion (starting at 1) and i! is the factorial of i.

The taylor_expansion function returns the approximation of the function at the given point using the Taylor series expansion with the specified number of terms.
'''
