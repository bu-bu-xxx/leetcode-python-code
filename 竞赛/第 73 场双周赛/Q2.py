# encoding:utf-8
# @Author :ZQY


# 5217. 将杂乱无章的数字排序
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = str(nums[i])
            tmp = ''
            for s in num:
                tmp += str(mapping[int(s)])
            nums[i] = (nums[i], int(tmp), i)

        nums = sorted(nums, key=lambda s: s[1:])
        return [a for a, b, i in nums]
