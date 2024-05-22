n=int(input())
b= [[0] * n for t in range(n)]
for i in range(n):
    b[i][0]=1
    b[i][i]=1
for i in range(n):
    for j in range(1,i):
        b[i][j]=b[i-1][j]+b[i-1][j-1]
for i in range(n):
    for j in range(i+1):
        print(b[i][j],end=' ')
    print()