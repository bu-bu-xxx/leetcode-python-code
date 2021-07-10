# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划，背包问题
# 评价标准[len,9num,...,1num]
from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[0] * 10] + [None] * target
        for i, val in enumerate(cost):
            for j in range(val, target + 1):
                if dp[j - val] is not None:
                    tmp = dp[j - val].copy()
                    tmp[0] += 1
                    tmp[-(i + 1)] += 1
                    dp[j] = max(dp[j], tmp) if dp[j] else tmp
        if dp[-1] is None:
            return '0'
        res = dp[-1]
        return '9' * res[1] + '8' * res[2] + '7' * res[3] + '6' * res[4] \
               + '5' * res[5] + '4' * res[6] + '3' * res[7] + '2' * res[8] \
               + '1' * res[9]


if __name__ == '__main__':
    try1 = Solution()
    cost1 = [4, 3, 2, 5, 6, 7, 2, 5, 5]
    target1 = 9
    print(try1.largestNumber(cost1, target1))
