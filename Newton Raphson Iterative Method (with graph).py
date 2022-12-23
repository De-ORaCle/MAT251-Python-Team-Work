import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, epsilon=1e-7, max_iter=100):
    x = x0
    iter = 0
    x_values = []
    y_values = []
    while True:
        x_values.append(x)
        y_values.append(f(x))
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < epsilon:
            break
        x = x_new
        iter += 1
        if iter == max_iter:
            break
    return x, x_values, y_values

def f(x):
    # example function
    return x**3 - 5*x -40

def df(x):
    # derivative of example function
    return 3*x**2 - 5

x0 = float(input("Enter the initial guess for x: "))
epsilon = float(input("Enter the tolerance: "))
max_iter = int(input("Enter the maximum number of iterations: "))

result, x_values, y_values = newton_raphson(f, df, x0, epsilon, max_iter)
print(f"Root of the equation is: {result}")

plt.plot(x_values, y_values, 'o-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton-Raphson method')
plt.show()
