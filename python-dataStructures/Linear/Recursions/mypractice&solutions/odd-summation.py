# Write a recursive function sum_odd(lis) that takes in a list of integers, and returns the sum of only odd numbers inside the list.

def sum_odd(lis):
    if not lis:
        return 0

    if lis[0] % 2 != 0:
        return lis[0] + sum_odd(lis[1:])
    else:
        return sum_odd(lis[1:])
    
    print(tot)


print(sum_odd([1,2,3,4])  )  # 4
print(sum_odd([1,2,3,4,5]))  # 9
print(sum_odd([1,2,4,6,8]))  # 1
print(sum_odd([])         )  # 0
print(sum_odd([2,4,6,8])  )  # 0