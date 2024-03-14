def nesLst(arr):
    return sorted([each[0] for each in arr if sorted(set([each[1] for each in arr]),reverse=False)[1] in each])

if __name__ == "__main__":
    # data = []
    # n = int(input())
    # for each in range(n):
    #     name = str(input('Enter name: '))
    #     score = float(input(f"Enter {name}'s score: "))
    #     data.append([name,score])
    print(nesLst([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]))