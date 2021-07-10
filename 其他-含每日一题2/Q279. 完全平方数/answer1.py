# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划，背包问题
# 你的背包，背到现在还没烂
# 每次迭代所有平方数
import math


class Solution:
    def numSquares(self, n: int) -> int:
        nums = [s ** 2 for s in range(1, math.floor(n ** 0.5) + 1)]
        dp = [0] + [10 ** 5] * n
        for num in nums:
            for i in range(num, n + 1):
                dp[i] = min(dp[i - num] + 1, dp[i])
        return dp[n]
