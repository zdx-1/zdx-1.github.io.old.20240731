ans = 0
def dfs(depth, n, m):
    global ans
    if depth == 7:
        if n == 0 and m == 0:
            ans += 1
        return
    for i in range(n + 1):
        for j in range(m + 1):
            if 2 <= i + j <= 5 and i <= n and j <= m:
                dfs(depth + 1, n - i, m - j)
dfs(0,9,16)
print(ans)
