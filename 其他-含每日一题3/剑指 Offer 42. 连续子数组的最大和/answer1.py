# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，前缀和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_min = 0
        res = -10000
        ans = 0
        for num in nums:
            ans += num
            res = max(res, ans - pre_min)
            pre_min = min(pre_min, ans)
        return res
