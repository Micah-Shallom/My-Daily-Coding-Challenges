def power(n,exp):
    assert exp>=0 and int(exp) == exp , "Only positive integers are required"
    if  exp in [0,1]:
        return n
    else:
        return n*(power(n,exp-1)) 

print(power(-3.4,3))