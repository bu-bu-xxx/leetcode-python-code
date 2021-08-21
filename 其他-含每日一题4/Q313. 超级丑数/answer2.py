# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案+动态规划
# 需要一定的数学证明
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * len(primes)
        res = [1]
        while len(res) != n:
            min_val = min([res[dp[i]] * primes[i] for i in range(len(primes))])
            res.append(min_val)
            for i in range(len(primes)):
                if min_val == res[dp[i]] * primes[i]:
                    dp[i] += 1

        return res[-1]
