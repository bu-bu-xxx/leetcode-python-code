# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划，背包问题
# dp[g][p]表示g个人赚p的利润的方法数
# 转移函数：
# 一般dp[g][p] += dp[g-group[i]][p-profit[i]]
# p == minProfit 求的是大于等于要求利润的所有方法数
# 初始dp[0][0] = 1
# 最终返回p大于等于minProfit的方法数和
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        # 迭代
        for i in range(len(group)):
            for g in range(n, group[i] - 1, -1):
                dp[g][minProfit] += sum(dp[g - group[i]][(minProfit - profit[i]):]) \
                    if minProfit >= profit[i] else sum(dp[g - group[i]])
            for p in range(minProfit - 1, profit[i] - 1, -1):
                for g in range(n, group[i] - 1, -1):
                    dp[g][p] += dp[g - group[i]][p - profit[i]]
        # 结果
        return sum([s[-1] for s in dp]) % mod
