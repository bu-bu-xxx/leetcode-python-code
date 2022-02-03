# encoding:utf-8
# @Author :ZQY


# 参考官方答案，BFS稍微改进
import collections
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]

        # 载入所有海洋
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    queue.append((i, j))

        # BFS
        while queue:
            node_tmp = queue.popleft()
            i, j = node_tmp[0], node_tmp[1]
            h_tmp = height[i][j]
            for nei_i, nei_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= nei_i < m and 0 <= nei_j < n and height[nei_i][nei_j] == -1:
                    height[nei_i][nei_j] = h_tmp + 1
                    queue.append((nei_i, nei_j))

        return height
