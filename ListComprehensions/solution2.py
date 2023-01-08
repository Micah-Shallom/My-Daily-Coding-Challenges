# using while loops

def listComp(x,y,z,n):
    arr = []
    i = 0
    while i <= x:
        j = 0 
        while j <= y:
            k = 0
            while k <= z:
                if i+j+k != n:
                    arr.append([i,j,k])
                k += 1
            j += 1
        i += 1
    return arr

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(listComp(x,y,z,n))