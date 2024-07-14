# Write a recursive function to reverse a string. For example, given the input "hello", the function should return "olleh".

def reverse(n):
    if n == "":
        return ""
    else: 
        return n[-1] + reverse(n[:-1])




print(reverse("hello"))