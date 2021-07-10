# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，单源最短路径
# Dijkstra算法
# 修改最短路径选取算法，relax函数
# 找到(0,0)到(m-1,n-1)最短距离即可
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        m, n = len(heights), len(heights[0])
        d = [[float("inf")] * n for _ in range(m)]
        d[0][0] = 0
        heap = [(0, 0, 0)]  # (val,i,j)
        dx_dy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def relax(i1: int, j1: int, i2: int, j2: int):
            if 0 <= i2 < m and 0 <= j2 < n and \
                    (new := max(abs(heights[i2][j2] - heights[i1][j1]), d[i1][j1])) < d[i2][j2]:
                d[i2][j2] = new
                heapq.heappush(heap, (new, i2, j2))

        while 1:
            tmp = heapq.heappop(heap)
            if tmp[1] == m - 1 and tmp[2] == n - 1:
                return tmp[0]
            for dx, dy in dx_dy:
                relax(tmp[1], tmp[2], tmp[1] + dx, tmp[2] + dy)
