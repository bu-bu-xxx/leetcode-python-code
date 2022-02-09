# encoding:utf-8
# @Author :ZQY


# 自己做，easy
import collections
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = collections.Counter()
        for num in nums:
            count[num] += 1

        res = 0
        for key, value in count.items():
            if value == 1:
                res += key

        return res
