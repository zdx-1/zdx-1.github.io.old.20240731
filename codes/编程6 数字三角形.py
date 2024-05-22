#递推算法
#通过栈实现
#dfs需要减值，不然会爆栈
#找到递归公式，自上而下的解决问题（自上而下计算）
#找到递归出口，就是递归的终止条件
#斐波那契数列
"""

递推式：f(n)=f(n-1)+f(n-2)
打印第20个数

递推实现：
a=[0,1]
res=0
for i in range(2,20):
    res+=1
    a.append(a[i-1]+a[i-2])
print(a[-1])
print(res)


递归实现：
cnt=0
def fib(n):
    global cnt
    cnt+=1
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(20))
print(cnt)


"""
'''
a=[[0]*101]*101
n=int(input())
for i in range(1,n+1):
    a[i]=input().split()
    a[i]=list(map(int,a[i]))
for i in range(n-1,0,-1):
  for j in range(0,i):
    if a[i+1][j] >=a[i+1][j+1]:
      a[i][j]+=a[i+1][j]
    else:
      a[i][j]+=a[i+1][j+1]
print(a[1][0])
'''
    

            

n = int(input())
a = [[0] * 101 for _ in range(101)]
for i in range(1, n+1):
    a[i] = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if a[i+1][j] >= a[i+1][j+1]:
            a[i][j] += a[i+1][j]
        else:
            a[i][j] += a[i+1][j+1]

print(a[1][0])


'''

# 读取数字三角形
n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

# 从倒数第二行开始计算最大和
for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

# 最大和即为顶部元素的值
max_sum = triangle[0][0]
print(max_sum)


'''

























