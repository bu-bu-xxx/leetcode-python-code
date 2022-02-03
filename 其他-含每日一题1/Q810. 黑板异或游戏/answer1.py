# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学
# 先判断是不是天胡，全部数异或和=0，直接win
# 不是的话，奇数输，偶数win，可证明
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        xor_sum = 0
        for i in nums:
            xor_sum ^= i
        if xor_sum == 0:
            return True
        return False
