def euler(f, t0, y0, h, n):
    """
    Approximate the solution of a first-order ODE using Euler's method.
    
    Parameters:
    f (function): The right-hand side of the ODE y' = f(t, y).
    t0 (float): The initial value of the independent variable t.
    y0 (float): The initial value of the dependent variable y.
    h (float): The step size.
    n (int): The number of steps to take.
    
    Returns:
    tuple: A tuple containing two lists, the first containing the t values and the second containing the corresponding y values.
    """
    t = [t0]
    y = [y0]
    
    for i in range(n):
        y_new = y[-1] + h * f(t[-1], y[-1])
        t_new = t[-1] + h
        t.append(t_new)
        y.append(y_new)
    
    return t, y

'''
To use this function, you will need to provide a function f that represents the right-hand side of the ODE, t0 and y0 which are the initial values of the independent and dependent variables, h which is the step size, and n which is the number of steps to take. The function will return a tuple containing two lists: the first list contains the values of the independent variable t at each step, and the second list contains the corresponding values of the dependent variable y.

Here's an example of how you can use this function to approximate the solution to the ODE y' = y with initial value y(0) = 1 over the interval [0, 1] with step size h = 0.1:
'''

def f(t, y):
    return y

t, y = euler(f, 0, 1, 0.1, 10)
print(t)
print(y)
