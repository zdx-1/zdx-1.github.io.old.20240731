def input_list():
    return list(map(int,input().split()))

n,m=input_list()
a=[]
for i in range(n):
    a.append(input_list())
b=[[0]*m for i in range(n)]

dir=[(1,0),(0,1),(0,-1),(-1,-1),(1,-1),(1,1)]

