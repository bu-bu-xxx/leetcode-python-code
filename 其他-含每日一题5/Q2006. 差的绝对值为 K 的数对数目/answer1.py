# encoding:utf-8
# @Author :ZQY


# 自己做，easy，哈希表
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        res = 0
        for num in nums:
            count[num] += 1
            res += count[num - k] + count[num + k]

        return res
