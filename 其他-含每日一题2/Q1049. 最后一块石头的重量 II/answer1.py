# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，背包问题，动态规划
# 总重量为N，任选其中几个石头，使得重量和最接近N/2
# 动态规划：state[i]表示能否到达i重量
# 每次遍历一个石头，就判断能不能到达这个重量
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        weight = sum(stones) // 2
        dp = [1] + [0] * weight
        for i in stones:
            if i <= weight:
                for j in range(weight, i - 1, -1):
                    dp[j] = max(dp[j], dp[j - i])
        for i, flag in enumerate(dp[-1::-1]):
            if flag == 1:
                return sum(stones) - 2 * (weight - i)
