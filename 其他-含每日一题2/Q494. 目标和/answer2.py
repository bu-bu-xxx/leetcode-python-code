# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，递归，暴力尝试
# 超出时间限制，用cpp就不会，太不公平了
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def bfs(index, sum_val):
            nonlocal count
            if index == len(nums) - 1:
                if sum_val == target:
                    count += 1
            else:
                index += 1
                bfs(index, sum_val + nums[index])
                bfs(index, sum_val - nums[index])

        bfs(-1, 0)
        return count
