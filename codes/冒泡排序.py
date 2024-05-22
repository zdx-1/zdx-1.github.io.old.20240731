n=int(input())
a=list(map(int,input().split()))
#循环n-1次,获得第i大
for i in range(1,n-1):
    #每次比较a[j]和a[j+1]
    for j in range(0,n-i):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(" ".join(map(str,a)))


n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
    for j in range(0,n-i):
        if a[j] >a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(" ".join(map(str,a)))
