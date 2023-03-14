# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，简单
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)) - 1 if 0 in nums else len(set(nums))
