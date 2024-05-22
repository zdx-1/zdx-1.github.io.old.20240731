#求出a的前缀和：
def get_presum(a):
    n=len(a)
    sum=[0]*n
    sum[0]=a[0]
    for i in range(1,n):
        sum[i]=sum[i-1]+a[i]
    return sum
#求出a[1]+……+a[r]的和
def get_sum(sum,l,r):
    if l==0:
        return sum[r]
    else:
        return sum[r]-sum[l-1]

a=[1,2,3,4,5]
sum=get_presum(a)
print("a=",a)
print("sum=",sum)
print(get_sum(sum,2,3))


#前缀和实现2
from itertools import accumulate
def get_presum(a):
    sum=list(accumulate(a))
    return sum
def get_sum(sum,l,r):
    if l==0:
        return sum[r]
    else:
        return sum[r]-sum[l-1]
a=[1,2,3,4,6]
sum=get_presum(a)
print("a=",a)
print("sum=",sum)
print(get_sum(sum,2,3))
