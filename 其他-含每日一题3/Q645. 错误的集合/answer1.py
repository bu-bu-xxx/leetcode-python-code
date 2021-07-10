# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，哈希表
# 简单
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = [0] * (n + 1)
        res = [0, 0]
        for num in nums:
            if check[num]:
                res[0] = num
            check[num] = 1
        res[1] = round(-sum(nums) + res[0] + (n + 1) * n / 2)
        return res
