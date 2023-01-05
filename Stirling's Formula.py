import math

def stirling(n: int) -> float:
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


n = float(input("Enter a number: "))
result = stirling(n)
print(f"The approximate factorial of {n} is {result}.")
