# encoding:utf-8
# @Author :ZQY


# 自己做，动态规划
from typing import List


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        nex = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

        def one_move(dp_old: List[List[int]]):
            dp_new = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for i_add, j_add in nex:
                        if 0 <= i + i_add < n and 0 <= j + j_add < n:
                            dp_new[i + i_add][j + j_add] += dp_old[i][j] / 8
            return dp_new

        # 棋盘上每个点的概率
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        for move in range(k):
            dp = one_move(dp)

        return sum([sum(s) for s in dp])
