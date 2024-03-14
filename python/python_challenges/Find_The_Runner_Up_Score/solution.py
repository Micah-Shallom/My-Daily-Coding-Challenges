def runUp(arr):
    return sorted(set(arr), reverse=True)[1]
    

if __name__ == "__main__" :
    n = int(input())
    arr = map(int,input().split())
    print(runUp(arr))