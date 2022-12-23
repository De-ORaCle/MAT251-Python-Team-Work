import matplotlib.pyplot as plt


def linear_iteration(f, g, x0, tol=1e-9, maxiter=100):
    """
    Use the linear iteration method to find a root of the equation f(x) = 0.

    Parameters
    ----------
    f : function
        The function whose root we are trying to find.
    g : function
        The function used to approximate the root in each iteration.
    x0 : float
        The initial guess for the root.
    tol : float, optional
        The tolerance for the error in the approximation of the root.
        The default value is 1e-9.
    maxiter : int, optional
        The maximum number of iterations to perform. The default value is 100.

    Returns
    -------
    float
        An approximation of the root of the function f.
    int
        The number of iterations performed.

    Raises
    ------
    ValueError
        If the initial guess is invalid (i.e., f(x0) = 0).
    """
    if f(x0) == 0:
        raise ValueError("The initial guess is invalid.")

    x = g(x0)
    num_iter = 0
    values = []
    while abs(f(x)) > tol and num_iter < maxiter:
        x = g(x)
        num_iter += 1
        values.append(x)

    return x, num_iter, values


# Example usage

def f(x):
    return x**2 - 3*x + 1


def g(x):
    return (1 +  x**2) / 3


root, num_iter, values = linear_iteration(f, g, 1.5)
print(f"Root: {root}")
print(f"Number of iterations: {num_iter}")

# Plot the results
plt.plot(values)
plt.xlabel("Iteration")
plt.ylabel("Approximation of root")
plt.title('Linear Iteration')
plt.show()
