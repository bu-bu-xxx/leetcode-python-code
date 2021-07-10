# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 非官方答案，SPFA
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[float('inf')] * n for _ in range(n)]
        queue = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return False
            return True

        for i in range(n):
            for j in range(n):
                if grid[i][j]:  # ->island
                    d[i][j] = 0
                    queue.append([i, j])

        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if isValid(next_x, next_y) and d[next_x][next_y] > d[x][y] + 1:
                    d[next_x][next_y] = d[x][y] + 1
                    if [next_x, next_y] not in queue:
                        queue.append([next_x, next_y])

        ans = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, d[i][j])

        return ans if ans != float('inf') else -1
