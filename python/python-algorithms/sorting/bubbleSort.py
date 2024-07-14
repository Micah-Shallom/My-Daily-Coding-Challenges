def bubblesort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    return customList


# cList = [3,6,8,12,4,9,1,0,6]
cList = [5,2,3,1]
print(bubblesort(cList))