# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，贪心算法
# ez
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ans = sorted(nums)
        res = len(nums)

        tmp = 0
        for i in range(len(nums)):
            if ans[i] == nums[i]:
                tmp += 1
            else:
                break

        res -= tmp
        if res == 0:
            return res

        tmp = 0
        for i in range(-1, -len(nums) - 1, -1):
            if ans[i] == nums[i]:
                tmp += 1
            else:
                break

        res -= tmp
        return res
