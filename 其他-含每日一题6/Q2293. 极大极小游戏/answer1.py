# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    nums[i] = min(nums[i * 2], nums[i * 2 + 1])
                else:
                    nums[i] = max(nums[i * 2], nums[i * 2 + 1])
            nums = nums[0:len(nums) // 2]
        return nums[0]
