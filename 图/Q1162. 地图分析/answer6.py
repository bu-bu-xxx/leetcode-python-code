# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 非官方答案
# Dijkstra算法，用堆排序，对于稀疏的路径矩阵
# 确定每个点都不是inf的值
# 这个比Dijkstra算法复杂度高一点
import heapq
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[float('inf')] * n for _ in range(n)]
        priority_queue = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(x, y):
            if x < 0 or x >= n or y < 0 or y >= n: return False
            return True

        for i in range(n):
            for j in range(n):
                if grid[i][j]:  # ->island
                    d[i][j] = 0
                    priority_queue.append([0, i, j])

        while priority_queue:
            step, x, y = heapq.heappop(priority_queue)
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if isValid(next_x, next_y) and d[next_x][next_y] > step + 1:
                    d[next_x][next_y] = step + 1
                    heapq.heappush(priority_queue, [step + 1, next_x, next_y])

        res = max(sum(d, []))
        if res == 0 or res == float('inf'):
            return -1
        return res


