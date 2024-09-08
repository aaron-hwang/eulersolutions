def nfactorial (n :int) -> int:
    if n >= 0:
        r = 1
        for i in range(1, n):
            r = r * i
        return r 
    else: 
        return -1

bigNum = nfactorial(100)
digitSum = 0
for digit in list(str(bigNum)):
    digitSum += int(digit)

print(digitSum)