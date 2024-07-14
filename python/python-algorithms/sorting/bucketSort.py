def bucketSort(customList):
    import math
    num_buckets = round(math.sqrt(len(customList))) 
    hash_bucket = dict()
    max_value = max(customList)

    for num in range(num_buckets):
        hash_bucket[num] = []
    
    for num in customList:
        bnum = math.ceil(num * num_buckets / max_value)
        if num == 0:
            bnum = 1
        hash_bucket[bnum-1].append(num)
    
    for k, val in hash_bucket.items():
        for i in range(len(val)):
            key = val[i]
            j = i-1
            while j >=0 and key < val[j]:
                val[j+1] = val[j]
                j -= 1
            val[j+1] = key
        hash_bucket[k] = val

    sorted_list = []

    for bucket in hash_bucket.values():
        sorted_list.extend(bucket)
    
    return sorted_list

    

cList = [5,3,4,3,4,9,1,6,0]
print(bucketSort(cList))