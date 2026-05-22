import re
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

for line in f1:
    obj = re.sub("['0-9']", "@",line)
    f2.write(obj)
f1.close()
f2.close()