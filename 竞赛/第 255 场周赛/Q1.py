# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5850. 找出数组的最大公约数
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def count(a,b):
            if a<b:
                b,a = a,b
            if a%b == 0:
                return b
            tmp = b
            b = a%b
            a = tmp
            return count(a,b)

        return count(max(nums),min(nums))



