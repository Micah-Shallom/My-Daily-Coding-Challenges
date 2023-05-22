# Write a Python program to convert an integer to a string in any base.

##################### Non Recursive Solution ######################################

# def convert_to_base(n, base):
#     if n == 0:
#         return '0'

#     result = ''
#     negative = False

#     if n < 0:
#         negative = True
#         n = abs(n)

#     while n > 0:
#         remainder = n % base
#         result = str(remainder) + result
#         n = n // base

#     if negative:
#         result = '-' + result

#     return result

# # Example usage
# print(convert_to_base(123, 2))   # Output: '1111011' (base 2)
# print(convert_to_base(123, 8))   # Output: '173' (base 8)


##################### Recursive Solution ######################################

def convert_to_base(n, base):
    if n == 0:
        return '0'

    if n < 0:
        return '-' + convert_to_base(abs(n), base)

    if n < base:
        return str(n) 
    return convert_to_base(n//base, base) + str(n % base)

print(convert_to_base(123, 2))   # Output: '1111011' (base 2)
print(convert_to_base(123, 8))   # Output: '173' (base 8)


