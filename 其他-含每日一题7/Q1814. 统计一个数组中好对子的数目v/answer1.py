# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
import collections
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = collections.Counter()
        for num in nums:
            num_rev = int(str(num)[-1::-1])
            count[num - num_rev] += 1

        res = 0
        for value in count.values():
            res += value * (value - 1) // 2

        mod = 10 ** 9 + 7
        return res % mod
