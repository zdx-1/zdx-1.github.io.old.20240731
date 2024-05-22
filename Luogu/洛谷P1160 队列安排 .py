class Node:
    def __init__(self, date, prev, next):
        self.date = date
        self.prev = prev
        self.next = next
        self.flag = True
N = int(input())
a = [None] * (N + 1)
a[0] = Node(0, a[0], a[0])
a[1] = Node(1, a[0], a[0])
a[0].next = a[1]
a[0].prev = a[1]
for i in range(2, N + 1):
    k, p = map(int, input().split())
    if p == 0:
        a[i] = Node(i, a[k].prev, a[k])
        a[k].prev.next = a[i]
        a[k].prev = a[i]
    else:
        a[i] = Node(i, a[k], a[k].next)
        a[k].next.prev = a[i]
        a[k].next = a[i]
M = int(input())
for i in range(M):
    x = int(input())
    a[x].flag = False
cur = a[0]
while cur.next != a[0]:
    cur = cur.next
    if cur.flag != False:
        print(cur.date, end=" ")