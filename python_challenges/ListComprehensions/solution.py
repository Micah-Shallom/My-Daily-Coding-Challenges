def listComp(x,y,z,n):
    arr = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n ]
    return arr


if __name__ == '__main__' :
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(listComp(x,y,z,n))