sert = 0
with open("data.txt") as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        if row[4] == "Latvia" and row[3].startswith("https://"):
            sert += 1
print(sert)