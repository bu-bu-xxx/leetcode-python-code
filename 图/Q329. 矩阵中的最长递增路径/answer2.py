# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，拓扑排序
# 复习
# 每次出队列出度为0的点，进行广度优先搜索
# 最后看迭代次数
import collections
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        def nexRoad(i, j):
            ret = []
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                ret.append((i - 1, j))
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                ret.append((i, j - 1))
            if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                ret.append((i + 1, j))
            if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                ret.append((i, j + 1))
            return ret

        def lastRoad(i, j):
            ret = []
            if i - 1 >= 0 and matrix[i][j] > matrix[i - 1][j]:
                ret.append((i - 1, j))
            if j - 1 >= 0 and matrix[i][j] > matrix[i][j - 1]:
                ret.append((i, j - 1))
            if i + 1 < m and matrix[i][j] > matrix[i + 1][j]:
                ret.append((i + 1, j))
            if j + 1 < n and matrix[i][j] > matrix[i][j + 1]:
                ret.append((i, j + 1))
            return ret

        out_all = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for nex in nexRoad(i, j):
                    out_all[i][j] += 1

        queue = collections.deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if out_all[i][j] == 0:
                    queue.append((i, j))

        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                for last in lastRoad(tmp[0], tmp[1]):
                    out_all[last[0]][last[1]] -= 1
                    if out_all[last[0]][last[1]] == 0:
                        queue.append(last)
            res += 1

        return res
