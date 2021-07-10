# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 未搜索0，已搜索用最大路线长度表示
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        state = [[0] * n for _ in range(m)]

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

        def dfs(i, j):
            if state[i][j] > 0:
                return state[i][j]

            state[i][j] = 1
            for nex in nexRoad(i, j):
                state[i][j] = max(state[i][j], dfs(nex[0], nex[1]) + 1)
            return state[i][j]

        for row in range(m):
            for col in range(n):
                dfs(row, col)

        return max(sum(state, []))
