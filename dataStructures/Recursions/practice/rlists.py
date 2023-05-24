# Write a Python program to sum recursion lists.

############################# Non Recursive Solution #############################
def nested_sum(nested_list):
    total_sum = 0
    stack = nested_list

    while stack:
        element = stack.pop()

        if isinstance(element,list):
            stack.extend(element)
        else:
            total_sum += element
        
    return total_sum
        
    

######################### Recursive Solution #####################################
def recursive_list_sum(nested_list):
    total_sum = 0

    for element in nested_list:
        if isinstance(element, list):
            total_sum += recursive_list_sum(element)
        else:
            total_sum += element
    return total_sum


 
my_list = [1, [2, [3, 4], 5], 6]
print(recursive_list_sum(my_list))  # Output: 21
print(nested_sum(my_list))  # Output: 21
