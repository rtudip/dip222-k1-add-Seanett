sk = []
with open("data.txt") as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        if row[4] == "Oman":
            sk.append(int(row[6]))
sk.sort()
print(sk[0])