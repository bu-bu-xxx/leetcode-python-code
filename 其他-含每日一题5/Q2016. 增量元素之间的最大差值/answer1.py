# encoding:utf-8
# @Author :ZQY

# 自己做，简单题
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = 0
        for num in nums:
            min_val = min(min_val, num)
            res = max(res, num - min_val)
        return res if res > 0 else -1
