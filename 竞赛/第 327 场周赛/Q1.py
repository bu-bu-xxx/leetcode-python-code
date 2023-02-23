# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6283. 正整数和负整数的最大计数
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for num in nums:
            if num> 0:
                pos += 1
            elif num < 0:
               neg += 1
        return max(pos, neg)