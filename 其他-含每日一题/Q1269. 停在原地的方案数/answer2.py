# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 动态规划，官方答案
# 用二维数组代替字典，每次计算当前位置和相邻位置的num和
# 用模10^9 + 7的剩余系作为num
# matrix[i][j]表示第i个step的第j个位置的数量

class Solution:
    def numWays(self, steps, arrLen):
        mod = 10 ** 9 + 7
        max_column = min(steps + 1, arrLen)
        matrix = [[0] * (max_column + 2), [0] * (max_column + 2)]
        matrix[0][0] = 1
        # 开始迭代
        for _ in range(steps):
            for j in range(max_column):
                matrix[1][j] = (matrix[0][j - 1] + matrix[0][j] + matrix[0][j + 1]) % mod
            matrix[0] = matrix[1]
            matrix[1] = [0] * (max_column + 2)
        # 输出
        return matrix[0][0]
