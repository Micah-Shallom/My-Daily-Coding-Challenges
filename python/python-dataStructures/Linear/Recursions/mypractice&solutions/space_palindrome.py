def is_pal(n):
    if " " in n: #remove all spaces on input
        return is_pal(n.replace(" ",""))
    
    return recursive_helper(n)
    

def recursive_helper(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return is_pal(n[1:-1])
    else:
        return False


print(is_pal('aba')    )  # True
print(is_pal('ab   a') )  # True
print(is_pal(' a z  a'))  # True

print(is_pal('ab a b') )  # False
print(is_pal('a a  ba'))  # False
print(is_pal('a z a a'))  # False