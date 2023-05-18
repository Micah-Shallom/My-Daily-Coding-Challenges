def power(n,exp):
    if  exp in [0,1]:
        return n
    else:
        return n*(power(n,exp-1))

print(power(5,3))