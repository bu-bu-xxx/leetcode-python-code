# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 二分查找，官方答案

# 设定mid值
# 每行每列都是递增的，从左下角开始向右，碰到大于mid值的向上
# 这样划过的区域大小就是小于等于mid的数量了，称作mid量
# 要找出mid量刚好大于等于k的mid
# 二分查找：
# mid量大于等于k，则right=mid
# mid量小于k，则left = mid+1
# 最终left=right即找到

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        def count_num(mid):
            j = 0
            num = 0
            for i in range(n - 1, -1, -1):
                while j < n and matrix[i][j] <= mid:
                    j += 1
                num += j
            return num

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left != right:
            mid = (left + right) // 2
            if count_num(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
