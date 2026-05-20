input = [0,0,1,2,0,3,0,0,4]
for i in range(len(input)):
    for j in range(len(input)-1):
        if input[j] == 0:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
    
print(input)