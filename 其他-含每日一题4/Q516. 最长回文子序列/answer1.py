# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# dp[i][j]表示从s[i]到s[j]最长回文子序列
# dp[i][i] = 1
# dp[i][j] = max(dp[i+1][j],
#                dp[i][j-1],
#                dp[i+1][j-1]+2 if s[i]==s[j])


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1],
                               dp[i + 1][j - 1] + 2 if s[i] == s[j] else 0)

        return dp[0][n - 1]
