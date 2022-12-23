import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-9, maxiter=100):
    """
    Use the bisection method to find a root of the function f within the
    given tolerance.

    Parameters
    ----------
    f : function
        The function whose root we are trying to find.
    a : float
        The lower bound of the interval in which we are searching for a root.
    b : float
        The upper bound of the interval in which we are searching for a root.
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
        If the initial interval is invalid (i.e., f(a) and f(b) have the same sign).
    """
    if f(a) * f(b) >= 0:
        raise ValueError("The initial interval is invalid.")

    x = (a + b) / 2
    num_iter = 0
    values = []
    while abs(f(x)) > tol and num_iter < maxiter:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        num_iter += 1
        values.append(x)

    return x, num_iter, values


# Example usage

def f(x):
    return 5*x**2 + 11*x - 17


root, num_iter, values = bisection(f, 0, 2)
print(f"Root: {root}")
print(f"Number of iterations: {num_iter}")

# Plot the results
plt.plot(values)
plt.xlabel("Iteration")
plt.ylabel("Approximation of root")
plt.title('Bisection Method')
plt.show()

