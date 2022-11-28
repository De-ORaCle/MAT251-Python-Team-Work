"""
f(x) = a(x^3) + b(x^2) + c(x) + d
where a, b , c are coefficients, d is a constant and x is a variable.

This program will request inputs for coefficients and the constant.
Then find the possible root using linear iteration.
"""

import math

print("Given the polynomial, \n f(x) = a(x^3) + b(x^2) + c(x) + d \nIf the polynomial is quadratic, let 'a' = 0 "
      "\nIf the polynomial is linear, let 'a' = 'b' = 0\n")

loop = 1    # loop is a variable

while loop == 1:    # as long as loop = 1, the program below repeats
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    d = input("d = ")

    # Change the values of a, b, c and d from strings to integers and filter for string errors

    check_a = any(map(str.isdigit, a))
    check_b = any(map(str.isdigit, b))
    check_c = any(map(str.isdigit, c))
    check_d = any(map(str.isdigit, d))

    if check_a and check_b and check_c and check_d is True:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        loop = 2    # the loop is broken when loop != 1
    else:
        print("\nYou entered something that isn't recognised as a number value for a, b, c, and/or d."
              "\nDue to this error, try again.\n")

xvar = 0
while True:
    xprev = xvar
    # noinspection PyUnboundLocalVariable
    xnpone = (-1 / c) * ((a * xvar ** 3) + (b * xvar ** 2) + d)

    xvar = xnpone
    xdif = xnpone - xprev
    if xdif < 0.0000001:
        break

rounded = math.ceil(xnpone*10000)/10000
print("\nThe root of the equation is", rounded)
