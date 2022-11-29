"""
f(x) = a(x^3) + b(x^2) + c(x) + d
where a, b , c are coefficients, d is a constant and x is a variable.

This program will request inputs for coefficients and the constant.
Then find the possible root using the Newton Raphson Iterative Method.
"""

from sympy import * 
import math

print("Given the polynomial, \n f(x) = a(x^3) + b(x^2) + c(x) + d \nIf the polynomial is quadratic, let 'a' = 0 "
      "\nIf the polynomial is linear, let 'a' = 'b' = 0\n")

loop = 1    # loop is a variable

while loop == 1:    # as long as loop = 1, the program below repeats
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    d = input("d = ")
    print("\nThere exists a root between two points (y,z). Define the points:")
    y = input("y = ")
    z = input("z = ")

    # Change the values of a, b, c and d from strings to integers and filter for string errors

    check_a = any(map(str.isdigit, a))
    check_b = any(map(str.isdigit, b))
    check_c = any(map(str.isdigit, c))
    check_d = any(map(str.isdigit, d))
    check_y = any(map(str.isdigit, y))
    check_z = any(map(str.isdigit, z))

    if check_a and check_b and check_c and check_d and check_y and check_z is True:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        y = float(y)
        z = float(z)
        loop = 2    # the loop is broken when loop != 1
    else:
        print("\nYou entered something that isn't recognised as a number value for a, b, c, and/or d."
              "\nDue to this error, try again.\n")

# noinspection PyUnboundLocalVariable
ysol = (a * (y ** 3)) + (b * (y ** 2)) + (c * y) + d
# noinspection PyUnboundLocalVariable
zsol = (a * (z ** 3)) + (b * (z ** 2)) + (c * z) + d

if ysol > 0 and zsol < 0:
	print("\n")
elif ysol < 0 and zsol > 0:
	print("\n")
elif ysol == 0:
	print("\nThe solution to the equation is", y)
elif zsol == 0:
	print("\nThe solution to the equation is", z)
elif ysol > 0 and zsol > 0:
	print("\nThe solutions of y and z seem to be positive. Therefore, there is no root between those points.")
	exit()
elif ysol < 0 and zsol < 0:
	print("\nThe solutions of y and z seem to be negative. Therefore, there is no root between those points")
	exit()
else:
	print("\nThere seem to be no root between the points y and z given.")
	exit()


myList = [ysol, zsol]
myNumber = 0

closest = min(myList, key=lambda x: abs(x-myNumber))

if ysol == closest:
	xnought = y
elif zsol == closest:
	xnought = z

x, p = symbols('x p') 
expr = (a * (x ** 3)) + (b * (x ** 2)) + (c * x) + d
expr_diff = Derivative(expr, x)   

derivativeSol = format(expr_diff.doit().subs({x:xnought}))
derivativeSol = float(derivativeSol)

xnought = xnought - ((a * (xnought ** 3)) + (b * (xnought ** 2)) + (c * xnought) + d) /derivativeSol

while True:
    xprev = xnought
    # noinspection PyUnboundLocalVariable
    xnpone = xnought - ((a * (xnought ** 3)) + (b * (xnought ** 2)) + (c * xnought) + d) /derivativeSol

    xnought = xnpone
    xdif = xnpone - xprev
    if xdif < 0.0000001:
        break

rounded = math.ceil(xnpone*10000)/10000
print("\nThe root of the equation is", rounded)
