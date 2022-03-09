# encoding:utf-8
# @Author :ZQY


# 6024. 数组中紧跟 key 之后出现最频繁的数字
import collections
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = collections.Counter()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == key:
                count[nums[i + 1]] += 1
        return max(count.keys(), key=lambda s: count[s])
