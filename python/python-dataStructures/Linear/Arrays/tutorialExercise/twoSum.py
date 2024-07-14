# def two_sum(nums, target):
#     seen = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[num] = i

##############recursive solution################################

def two_sum_recursive(nums, target, start_index=0, seen={}):
    if start_index == len(nums):
        return None
    
    complement = target - nums[start_index]

    if complement in seen:
        return [seen[complement], start_index]
    else:
        seen[nums[start_index]] = start_index

    return two_sum_recursive(nums, target,start_index + 1, seen)


# Test the function
nums = [2, 7, 11, 15]
target = 9
print(two_sum_recursive(nums, target))  # [0, 1]

################iterative solution########################
 
def two_sum(nums,target):
    seen = {}

    for idx, val in enumerate(nums):
        complement = target - val

        if complement in seen:
            return [seen[complement], idx]

        seen[val] = idx
    
    return seen
        
    
nums = [2, 11, 7, 15]
target = 9
print(two_sum(nums,target))
# print(two_sum([3,2,4],6))