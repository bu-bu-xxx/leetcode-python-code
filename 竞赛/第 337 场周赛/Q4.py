# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6321. 执行操作后的最大 MEX
import collections
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rec = collections.Counter()
        for i in range(value):
            rec[i] = 0
        for num in nums:
            rec[num % value] += 1

        tmp = min(rec.values())
        res = tmp * value - 1
        for v in range(value):
            rec[v] -= tmp
            if rec[v] > 0:
                res += 1
            else:
                break
        return res + 1
