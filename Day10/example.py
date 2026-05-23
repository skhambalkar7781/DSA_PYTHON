def string_compress(s):
    result = ""
    count = 1
    
    for i in range(len(s)):
        if i<len(s)-1 and s[i] == s[i+1]:
            count+=1
        else:
            result +=s[i]
            if count > 1:
                result+=str(count)
                
            count = 1
    return result
s = input("Enter the string: ")
print(string_compress(s))
