n=int(input())
a=list(input() for _ in range(n))
a.sort()
cout=0
while a:
    if len(a)==1:
        cout+=1
        break
    if a[0]!=a[1]:
        cout+=1
        a.pop(0)
    else:
        a.pop(0)
print(cout)


n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
 
count = n
for i in range(1, n):
    if lst[i] == lst[i - 1]:
        count -= 1
 
print(count)