s = "hello world"
words = s.split()
for word in words:
    rev = " "
    
    for i in range(len(word)-1, -1, -1):
        rev += word[i]

    print(rev, end=" ")