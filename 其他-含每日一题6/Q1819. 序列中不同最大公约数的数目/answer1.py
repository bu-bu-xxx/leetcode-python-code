# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 数学方法
# 复杂度计算涉及调和级数求和
import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        nums_list = [False] * (max_val + 1)
        for num in nums:
            nums_list[num] = True

        res = 0
        for i in range(1, max_val + 1):
            gcd_tmp = 0
            for j in range(i, max_val + 1, i):
                if nums_list[j] is True:
                    if gcd_tmp == 0:
                        gcd_tmp = j
                    else:
                        gcd_tmp = math.gcd(gcd_tmp, j)
                    if gcd_tmp == i:
                        res += 1
                        break
        return res
