# Write a function remove_vowels(string) that takes in a string, and returns only the non-vowels.

def remove_vowels(n):
    vowels = "aeiou"

    if len(n) == 0:
        return ""
    
    if n[0] not in vowels:
        return n[0] + remove_vowels(n[1:])
    else:
        return remove_vowels(n[1:])
    

print(remove_vowels('apple')    ) # ppl
print(remove_vowels('orange')   ) # rng
print(remove_vowels('pear')     ) # pr
print(remove_vowels('pineapple')) # pnppl
print(remove_vowels('durian')   ) # drn
print(remove_vowels('banana')   ) # bnn