# def string_reversal(s: str) -> str:
#     if s == "":
#         return ""
#     return string_reversal(s[1:]) + s[0]
# print(string_reversal("hello"))

def palindrome(s:str):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[len(s)-1]:
        return palindrome(s[1:len(s)-1])
    return False
print(palindrome("racecars"))