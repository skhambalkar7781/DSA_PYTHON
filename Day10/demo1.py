# # import re
# # count = 0
# # pattern = re.compile("Function")

# # matcher = pattern.finditer("A function in python in defined by a def statement python. The general syntax looks like this")

# # for i in matcher:
# #     print(i.group())
# #     count += 1

# #     print(i.start(),"..........",i.end(),"..........",i.group())
# # print("Total number of occurences are: ",count)

# # ===========================================================================
# import re
# count = 0
# matcher  = re.finditer("Hi","HiHiHiHiHiHi")

# for i in matcher:
#     print(i.group())
#     count += 1

#     print(i.start(),"..........",i.end(),"..........",i.group())
# print("Total number of occurences are: ",count)

# ======================================================================================
# import re
# obj = input("Enter any character:  ")
# objmatch = re.finditer(obj,"a7b @k9z")
# print(objmatch)
# for match in objmatch:
#     print(match.start(),"..........",match.end(),"..........",match.group())
    
# ======================================================================================

# for checking first character of sentence

# import re

# a = input("Enter string to perfrom match character: ")
# mtch = re.finditer(a,"python is a programming language")

# print(mtch)

# for m in mtch:
#     if m != None:
#         print("match found at beginning")
#         print(m.start(), " ",m.end())
#     else:
#         print("There is no match found at beginning")
    
# =====================================================================================


# import re 
# s = input("Enter mobile number: ")
# obj = re.fullmatch("[0-5]\d{9}",s)
# if obj != None:
#     print("Mobile number is valid")
# else:
#     print("Mobile number is invalid")
    
# =======================================================================

# import re 
# a = input("Enter string to perform : ")
# mtch = re.search(a,"python ss dynamic lann")
# print(mtch)
# if mtch != None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("There is no match found")

# ======================================================================

# import re
# mtch = re.findall('[A-Z]',"abcd3jfhZyfhhdQ*&^%")
# print(mtch) 

# =========================================

import re
obj =re.sub('[a-z]','*','2345 ABCD habc deff')
print(obj)
# =================================

import re
obj =re.subn('[0-7]','@','ab3g')
print(obj)
