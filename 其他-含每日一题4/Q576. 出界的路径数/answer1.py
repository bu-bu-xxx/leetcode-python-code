# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        res = 0
        mod = 10 ** 9 + 7
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp[startRow][startColumn] = 1

        for _ in range(maxMove):
            dp_tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    for di, dj in direction:
                        if di + i < 0 or di + i >= m or dj + j < 0 or dj + j >= n:
                            res += dp[i][j]
                        else:
                            dp_tmp[di + i][dj + j] += dp[i][j]
            dp = dp_tmp

        return res % mod
