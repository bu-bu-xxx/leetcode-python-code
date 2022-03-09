# encoding:utf-8
# @Author :ZQY


# 自己做，冲冲冲
import collections
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # 特殊情况
        if n == 1:
            return [-1]

        state = collections.defaultdict(list)  # 每个位置有哪几个球
        for j in range(n):
            state[j].append(j)

        for row in range(m):
            state_nex = collections.defaultdict(list)
            for column in state.keys():
                if column == 0 and grid[row][column] == 1 and grid[row][column + 1] == 1:
                    state_nex[column + 1] += state[column]
                elif column == n - 1 and grid[row][column] == -1 and grid[row][column - 1] == -1:
                    state_nex[column - 1] += state[column]
                elif 0 < column < n - 1:
                    if grid[row][column] == 1 and grid[row][column + 1] == 1:
                        state_nex[column + 1] += state[column]
                    elif grid[row][column] == -1 and grid[row][column - 1] == -1:
                        state_nex[column - 1] += state[column]
            state = state_nex

        res = [-1] * n
        for des in state.keys():
            for beg in state[des]:
                res[beg] = des
        return res
