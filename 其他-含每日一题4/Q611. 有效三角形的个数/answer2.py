# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，排序 + 双指针
# answer1的升级版
import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0
        for a in range(n):
            c = a + 1
            for b in range(a + 1, n):
                c = max(bisect.bisect_left(nums, nums[a] + nums[b], lo=c) - 1, b)
                res += c - b

        return res
