def insertionSort(customList):

    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1  

        customList[j+1] = key
        
    return customList




cList = [3,1,8,12,4,9,1,0,6]
# cList = [5, 7, 4, 6, 1, 3]
print(insertionSort(cList))