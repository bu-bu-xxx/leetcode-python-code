# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，dfs或bfs，二分法
# 每次给个上限边权值
# 深度优先搜索：存当前点到已搜索点集，然后搜索nex点，当nex点未在已搜索集中and边权小于上限
# 看已搜索点集有没有终点
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        m, n = len(heights), len(heights[0])
        min_val, max_val = 0, 10 ** 6
        dx_dy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            search.add((i, j))
            for dx, dy in dx_dy:
                nex = (i + dx, j + dy)
                if 0 <= nex[0] < m and 0 <= nex[1] < n and nex not in search \
                        and abs(heights[i][j] - heights[nex[0]][nex[1]]) <= mid_val:
                    dfs(nex[0], nex[1])

        while min_val != max_val:
            mid_val = (min_val + max_val) // 2
            search = set()
            dfs(0, 0)
            if (m - 1, n - 1) in search:
                max_val = mid_val
            else:
                min_val = mid_val + 1

        return min_val
