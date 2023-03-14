# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，枚举
# https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/solution/an-wei-yu-wei-ling-de-san-yuan-zu-by-lee-gjud/
# x = (2**16-1) ^ nums[i] 01逆转
# sub = (sub-1)&x 神之一手
import collections
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        rec = collections.Counter()
        res = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                rec[nums[i]&nums[j]]+=1

        for i in range(len(nums)):
            for key in rec.keys():
                if key&nums[i] == 0:
                    res += rec[key]

        return res





