# # Write a function pascal(n) that takes in a positive integer n and returns the nth row of Pascal’s triangle.

############## non recursive solution #########################

def npascal(n):
    row_before = [1]

    for x in range(1, n+1):
        row_inner = [1]

        for y in range(1,x):
            row_inner.append(row_before[y-1] + row_before[y])

        row_inner.append(1)
        row_before = row_inner
    return row_before


############## recursive solution #############################
###i couldnt write this myself,,, so i will come back to it

def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        previous_row = pascal(n - 1)
        current_row = [1]
        for i in range(1, n):
            current_row.append(previous_row[i - 1] + previous_row[i])
        current_row.append(1)
        return current_row

    
    
    
    

    


    



# print(pascal(0))  # [1]
# print(pascal(1))  # [1, 1]
# print(pascal(2))  # [1, 2, 1]
# print(pascal(3))  # [1, 3, 3, 1]
# print(pascal(4))  # [1, 4, 6, 4, 1]
print(pascal(5))  # [1, 5, 10, 10, 5, 1]

