# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简化版动态规划
import math


class Solution:
    def numSquares(self, n: int) -> int:
        nums = [s ** 2 for s in range(1, math.floor(n ** 0.5) + 1)]
        dp = [0] + [10 ** 5] * n
        for i in range(1, n + 1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i - num] + 1, dp[i])
                else:
                    break
        return dp[n]
