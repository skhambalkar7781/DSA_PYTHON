input = [4,3,2,7,8,2,1,5,5]
newlist = []
count = 0
for i in range(0, len(input)):
    for j in range(i+1, len(input)):
        
        if input[i]== input[j]:
            newlist.append(input[i])
print(newlist)