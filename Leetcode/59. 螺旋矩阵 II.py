from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        left,right,up,down=0,n-1,0,n-1
        cnt=1
        while cnt <=n**2:
            #从左到右
            for i in range(left,right+1):
                res[up][i]=cnt
                cnt+=1
            up+=1
            #从上到下
            for i in range(up,down+1):
                res[i][right]=cnt
                cnt+=1
            right-=1
            #从右到左
            for i in range(right,left-1,-1):
                res[down][i]=cnt
                cnt+=1
            down-=1
            #从下到上
            for i in range(down,up-1,-1):
                res[i][left]=cnt
                cnt+=1
            left+=1
        return res

solution = Solution()
result = solution.generateMatrix(5)
for i in result:
    for j in i:
        print(j,end="\t")
    print()
