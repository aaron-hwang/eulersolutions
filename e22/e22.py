f = open(r"C:\Users\aaron\pythonstuff\projeuler\e22\0022_names.txt", "r")
raw = f.read().split(",")
for i, s in enumerate(raw):
    raw[i] = s.strip('\"')
raw.sort()
totalScore = 0
def alphabeticalScore(s : str):
    score = 0
    for c in s:
        score += ord(c) - 64
    return score
for j in range(len(raw)):
    totalScore += alphabeticalScore(raw[j]) * (j + 1)
print(totalScore)