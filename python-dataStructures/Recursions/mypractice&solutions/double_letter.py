# Write a function double(string) that takes in a string, and returns another version of the string where all letters are doubled.

def double(n):
    # return ''.join([each+each for each in n] #non-recursive solution

    if len(n) == 0:
        return ""
    # return n[0]+ n[0] + double(n[1:]) #a little less optimized
    return n[0]*2 + double(n[1:]) #more optimized
    

print(double('apple') )  # aappppllee
print(double('orange'))  # oorraannggee
print(double('pear')  )  # ppeeaarr
print(double('abc')   )  # aabbcc
print(double('zz')    )  # zzzz