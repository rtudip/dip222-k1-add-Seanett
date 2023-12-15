sk = []
with open("data.txt") as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        if row[4] == "Latvia" and row[7] == "Telecommunications":
            sk.append(int(row[8]))
print(sum(sk))