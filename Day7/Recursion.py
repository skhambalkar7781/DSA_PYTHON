# def factorial(num):
#     if num <=1:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(4))

# =========================================================================

# def capitalize(arr):
#     result =[]
#     if len(arr)==0:
#         return result
    
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalize(arr[1:])

# print(capitalize(['hello', 'world', 'python']))

# # ===========================================================
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent-1)

# print(power(2, 3))
# print(power(3, 4))
# print(power(2, 0))
# =====================================================

# def productofArray(arr):
#     if len(arr) ==0:
#         return 1
#     else:
#         return arr[0] * productofArray(arr[1:])
    
# print(productofArray([1,2,3,10]))
# print(productofArray([10,20]))
# =============================================================

# def reverse(string):
#     if len(string) <= 1:
#         return string
#     else:
#         return string[len(string)-1]+ reverse(string[0:len(string)-1])
    
# print(reverse('hello'))
# print(reverse('python'))

# ===============================================================================

# def recursiveRange(num):
#     if num <=0:
#         return 0
#     else:
#         return num + recursiveRange(num-1)

# print(recursiveRange(6))
# =================================================================================

def isPalindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    else:
        return isPalindrome(string[1:-1])
# ==================