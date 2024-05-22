import bisect
n,c = map(int,input().split())
lst0 = list(map(int,input().split()))
lst0.sort() #此方法用到了二分查找,所以需要先对列表进行排序
lst1 = [0 for i in range(n)]
for i in range(n):
    lst1[i] = lst0[i]-c
count = 0
for i in range(n):
    x = bisect.bisect_left (lst0,lst1[i])
    y = bisect.bisect_right(lst0,lst1[i])
    count += y-x
print(count)
