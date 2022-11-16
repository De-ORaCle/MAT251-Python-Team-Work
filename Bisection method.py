"""
f(x) = a(x^3) + b(x^2) + c(x) + d
where a, b , c are coefficients, d is a constant and x is a variable.

This program will request inputs for coefficients and the constant.
Then find the possible root using the bisection method.
"""

import sys

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

x1 = -1
x2 = 0
x3 = 1
x4 = 2
x5 = 3
# noinspection PyUnboundLocalVariable
fx1 = (a * (x1 ** 3)) + (b * (x1 ** 2)) + (c * x1) + d
fx2 = (a * (x2 ** 3)) + (b * (x2 ** 2)) + (c * x2) + d
fx3 = (a * (x3 ** 3)) + (b * (x3 ** 2)) + (c * x3) + d
fx4 = (a * (x4 ** 3)) + (b * (x4 ** 2)) + (c * x4) + d
fx5 = (a * (x5 ** 3)) + (b * (x5 ** 2)) + (c * x5) + d

print("\nFrom the values given above, it can be deduced that: ")
print("f(-1) = ", fx1)
print("f(0) = ", fx2)
print("f(1) = ", fx3)
print("f(2) = ", fx4)
print("f(3) = ", fx5)

# Next step, is to find the two values closest to zero amongst the above found values.
# The code below puts the solutions in a list and returns the positive and negative numbers closest to zero
fxes = [fx1, fx2, fx3, fx4, fx5]
maxn = sys.maxsize
minn = -sys.maxsize - 1
f = 0
for i in range(len(fxes)):
    if fxes[i] == 0:
        ans = 0
        f = 1
        break
    elif 0 < fxes[i] < maxn:
        maxn = fxes[i]
    elif 0 > fxes[i] > minn:
        minn = fxes[i]
    else:
        # noinspection PyStatementEffect
        None

# Recall which solutions gave the result 'maxn' and 'minn'

if maxn == fx1:
    fxmax_sol = "f(-1)"
    fxpos = -1
elif maxn == fx2:
    fxmax_sol = "f(0)"
    fxpos = 0
elif maxn == fx3:
    fxmax_sol = "f(1)"
    fxpos = 1
elif maxn == fx4:
    fxmax_sol = "f(2)"
    fxpos = 2
elif maxn == fx5:
    fxmax_sol = "f(3)"
    fxpos = 3
else:
    print("This code ran into issues solving your problem. This might be because there are no positive values "
          "between the solutions of f(-1) and f(3) for the polynomial given. \nThe program will terminate")
    exit()

if minn == fx1:
    fxmin_sol = "f(-1)"
    fxneg = -1
elif minn == fx2:
    fxmin_sol = "f(0)"
    fxneg = 0
elif minn == fx3:
    fxmin_sol = "f(1)"
    fxneg = 1
elif minn == fx4:
    fxmin_sol = "f(2)"
    fxneg = 2
elif minn == fx5:
    fxmin_sol = "f(3)"
    fxneg = 3
else:
    print("This code ran into issues solving your problem. This might be because there are no negative values "
          "between the solutions of f(-1) and f(3) for the polynomial given. \nThe program will terminate.")
    exit()

print("\nFrom the solution above, we can deduce the negative and positive solutions closest to zero. Which are: ")
# noinspection PyUnboundLocalVariable
print(fxmin_sol, " = ", minn)
# noinspection PyUnboundLocalVariable
print(fxmax_sol, " = ", maxn)

# noinspection PyUnboundLocalVariable
fxmainsol = (fxpos + fxneg)/2
fxbisect = (a * (fxmainsol ** 3)) + (b * (fxmainsol ** 2)) + (c * fxmainsol) + d

while fxbisect != 0:
    if fxbisect > 0:
        fxpos = fxmainsol
    elif fxbisect < 0:
        fxneg = fxmainsol

    fxmainsol = (fxpos + fxneg) / 2
    fxbisect = (a * (fxmainsol ** 3)) + (b * (fxmainsol ** 2)) + (c * fxmainsol) + d

print("\nTherefore the root of the solution is ", fxmainsol)
