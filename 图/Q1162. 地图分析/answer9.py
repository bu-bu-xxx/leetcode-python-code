# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，动态规划
# 每个D[i][j]记录离陆地的距离
# 1.从左往右，从上往下迭代
# D[i][j] = 0 if is land
#           min(D[i][j],D[i-1][j],D[i][j-1]) if is ocean
# 2.从右往左，从下往上
# D[i][j] = 0 if is land
#           min(D[i][j],D[i+1][j],D[i][j+1]) if is ocean
# 备注：用归纳法可以证明D是来自四个方向的最小值，结论还是没那么直观的，需要证明
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        inf_num = 1000
        n = len(grid)

        for i in range(n):
            for j in range(n):
                grid[i][j] = 0 if grid[i][j] == 1 else inf_num

        for i in range(n):
            for j in range(n):
                grid[i][j] = min(grid[i][j],
                                 grid[i - 1][j] + 1 if i - 1 >= 0 else inf_num,
                                 grid[i][j - 1] + 1 if j - 1 >= 0 else inf_num)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                grid[i][j] = min(grid[i][j],
                                 grid[i + 1][j] + 1 if i + 1 < n else inf_num,
                                 grid[i][j + 1] + 1 if j + 1 < n else inf_num)

        res = max(sum(grid, []))
        if res == 0 or res == inf_num:
            return -1
        return res


if __name__ == "__main__":
    try1 = Solution()
    grid1 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(try1.maxDistance(grid1))
