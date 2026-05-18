ar = [20,12,10,15,2]
for i in range(len(ar)):
    min = i
    j = i+1
    while j<len(ar):
        if ar[min] > ar[j]:
            min = j
        j+=1
        ar[i],ar[min] = ar[min],ar[i]
print(ar)