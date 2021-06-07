# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Q2
# 5777. 使数组元素相等的减少操作次数
from typing import List
import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        i = 0
        res = 0
        for key in sorted(count):
            res += i * count[key]
            i += 1
        return res
