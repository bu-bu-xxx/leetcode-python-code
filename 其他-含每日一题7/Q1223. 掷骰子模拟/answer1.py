# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，动态规划
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = []
        for i in range(6):
            dp.append([0] + [1] + [0] * (rollMax[i] - 1))

        for _ in range(n - 1):
            dp_nex = [[0] * (rollMax[s] + 1) for s in range(6)]
            tmp_sum = sum([sum(s[1:]) for s in dp])
            for i in range(6):
                for j in range(1, rollMax[i] + 1):
                    if j != 1:
                        dp_nex[i][j] += dp[i][j - 1]
                        dp_nex[i][j] %= mod
                    else:
                        dp_nex[i][j] += tmp_sum - sum(dp[i][1:])
                        dp_nex[i][j] %= mod
            dp = dp_nex

        return sum([sum(s) for s in dp]) % mod
