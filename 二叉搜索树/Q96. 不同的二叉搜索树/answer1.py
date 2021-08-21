# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学
# dp[n] = sigma(s[i]*s[n-1-i])  i in [0,n-1]


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        for i in range(3, n + 1):
            dp.append(sum([dp[j] * dp[i - 1 - j] for j in range(i)]))

        return dp[n]
