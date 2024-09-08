def selfPower(n :int):
    total = 0
    for i in range(1, n + 1):
        total += i**i
    return total
# trivial in python since we have arbitrary precision numbers
print(str(selfPower(1000))[-10:])