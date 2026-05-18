input = {"C": 3, "B": 2, "A": 1}

for i in input:
    ascending = sorted(input.items())
    descending = sorted(input.items(),reverse=True)
print(ascending)
print(descending)

    