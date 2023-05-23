# Write a Python program to sum recursion lists.

############################# Non Recursive Solution #############################
def nested_list_sum(nested_list):
   arr = nested_list
   total = 0

   while arr:
        each = arr.pop()

        if isinstance(each, list):
            arr.extend(each)
        else:
            total += each
   return total

######################### Recursive Solution #####################################
    
 
my_list = [1, [2, [3, 4], 5], 6]
print(nested_list_sum(my_list))  # Output: 21
