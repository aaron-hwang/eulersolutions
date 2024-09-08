import math

def digitFactorialSum(n: int):
    total = 0
    for c in str(n):
        total += math.factorial(int(c))
    return total

digitFactorials = []
# Obvious lowerbound is 10 since single digit factorials such as 1! don't count according to problem description
# Intuition says 9! as an upperbound is good enough (proof by guessing)
# 9! = 362880, 
for i in range(10, math.factorial(9)):
    if digitFactorialSum(i) == i:
        digitFactorials.append(i)

print(sum(digitFactorials))