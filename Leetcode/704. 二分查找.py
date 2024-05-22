#二分法
'''
前提：有序数组，也就是需要排序，且数组中没有重复元素

区间的定义：
    左闭右闭[left,right]
    左闭右开[left,right]
针对上面两种区间，以下是两种二分的写法实现
'''
#二分法的第一种写法
'''
定义target在一个左闭右闭[left,right]区间中
满足：
    while(left<=right)
    if(nums[middle]>target)  right要赋值为middle-1
    
'''
# 定义 Solution 类
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

# 创建 Solution 实例
solution = Solution()

# 调用 search 方法进行二分查找
a = [-1, 0, 3, 5, 9, 10]
target = 0
result = solution.search(a, target)
print("目标值在列表中的索引为:", result)



#二分法的第二种写法
'''
定义target在一个左闭右开[left,right]区间中
满足：
    while(left<right)
    if(nums[middle]>target)  right要赋值为middle
'''
# 定义 Solution 类
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

# 创建 Solution 实例
solution = Solution()

# 调用 search 方法进行二分查找
a = [-1, 0, 3, 5, 9, 10]
target = 0
result = solution.search(a, target)
print("目标值在列表中的索引为:", result)
