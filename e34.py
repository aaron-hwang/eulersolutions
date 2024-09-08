import math

def digitFactorialSum(n: int):
    total = 0
    for c in str(n):
        total += math.factorial(int(c))
    return total

digitFactorials = []
for i in range(10, math.factorial(9)):
    if digitFactorialSum(i) == i:
        digitFactorials.append(i)

print(sum(digitFactorials))