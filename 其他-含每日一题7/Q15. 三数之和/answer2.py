# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 动态规划，改良
import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        if len(nums) < 3:
            return res
        record = collections.defaultdict(set)
        record[nums[0] + nums[1]].add((nums[0], nums[1]))

        for i in range(2, len(nums)):
            val = nums[i]
            for s in record[-val]:
                res.add(s + (val,))
            for j in range(0, i):
                val2 = nums[j]
                record[val2 + val].add((val2, val))

        return [list(s) for s in list(res)]
