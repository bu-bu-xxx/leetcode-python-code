# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，动态规划
# 稍微调整一下，更简单
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [10 ** 5] * n
        ranges_list = list()
        for i, val in enumerate(ranges):
            ranges_list.append((max(0, i - val), min(n, i + val)))

        ranges_list = sorted(ranges_list)

        for left, right in ranges_list:
            for i in range(left, right + 1):
                dp[i] = min(dp[i], dp[left] + 1)

        return -1 if dp[-1] >= 10 ** 5 else dp[-1]
