# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，冲冲冲
# ez题目
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        return max([nums[i] + nums[n - 1 - i] for i in range(n // 2)])
