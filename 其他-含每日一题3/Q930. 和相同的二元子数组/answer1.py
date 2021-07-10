# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，前缀和，哈希表
# 我是sb
import collections
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        pre = collections.Counter()
        pre[0] += 1
        sum_val = 0
        for num in nums:
            sum_val += num
            res += pre[sum_val - goal]
            pre[sum_val] += 1
        return res
