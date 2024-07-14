# Write a function is_palindrome(string) that takes in a string, and returns True if the string is a palindrome, and False otherwise.


#################### Non Recursive Solution ############################

# def is_palindrome(str):
#     astr = list(str)
#     newstr = ''
#     lens = len(astr)-1
#     for idx,each in enumerate(astr):
#         newstr += astr[lens-idx]
#     if newstr == str:
#         return True
#     return False

####################Optimized Non Recursive Solution ############################

# def is_palindrome(str):
#     length = len(str)

#     for i in range(length // 2):
#         if str[i] != str[length-1-i]:
#             return False
#     return True


################### Recursive Solution #########################################

def is_palindrome(n):
    if len(n) <=1 :
        return True
    if n[0] == n[-1]:
        return is_palindrome(n[1:-1])
    else:
        return False
    
    

print(is_palindrome('aba'))     # True
print(is_palindrome('abba') )   # True
print(is_palindrome('abcba'))   # True

print(is_palindrome('abc')  )   # False
print(is_palindrome('abbb') )   # False
print(is_palindrome('abab') )   # False