# Write a recursive function sum_sub(lis) that takes in a list of integers. This function sums all odds numbers, and subtracts all even numbers, and returns the final output.

def sum_sub(lst):

    if not lst:
        return 0
    
    if lst[0] % 2 == 0:  #even condition
        return lst[0] - sum_sub(lst[1:])
    
    else: #odd condition
        return lst[0] + sum_sub(lst[1:])
    


print(sum_sub([1,2,3,4])   )# -2 
print(sum_sub([1,2,3,4,5])) # 3
print(sum_sub([1,3,5])   )  # 9
print(sum_sub([2,4,6])     )# -12
print(sum_sub([99,10,10]) ) # 79