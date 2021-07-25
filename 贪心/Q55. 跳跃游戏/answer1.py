# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，ez
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, val in enumerate(nums):
            if far >= i:
                far = max(far, i + val)
        return far >= len(nums) - 1
