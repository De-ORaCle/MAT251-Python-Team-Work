def composite_trapezoidal_rule(f, a, b, n):
    """
    Approximates the definite integral of f from a to b using the composite trapezoidal rule with n intervals.
    
    Parameters
    ----------
    f : function
        The function to be integrated.
    a : float
        The lower limit of the integral.
    b : float
        The upper limit of the integral.
    n : int
        The number of intervals to use in the composite trapezoidal rule.
    
    Returns
    -------
    float
        The approximate value of the definite integral of f from a to b using the composite trapezoidal rule with n intervals.
    """
    h = (b - a) / n  # calculate the interval size
    sum = 0.5 * (f(a) + f(b))  # initialize the sum with the terms at the ends of the interval
    
    # loop through the middle intervals and add their contributions to the sum
    for i in range(1, n):
        sum += f(a + i * h)
    
    return sum * h  # return the final result

'''
To use this function, you would simply need to define a function for the function you want to integrate (f), and provide values for the lower and upper limits of the integral (a and b), and the number of intervals to use (n).

For example, to approximate the integral of x^2 from 0 to 1 using 10 intervals, you could call the function like this:
'''

result = composite_trapezoidal_rule(lambda x: x**2, 0, 1, 10)
print(result)

#This would approximate the integral of f(x) = x**2 from 0 to 1 using 100 subintervals, and print the result.
