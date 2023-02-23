# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/solution/bu-hui-zi-dian-shu-zhi-yong-ha-xi-biao-y-p2pu/
# 顶级做法，哈希表
import collections
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        cnt = collections.Counter(nums)
        res = 0
        high_bit = 15
        low -= 1

        for x in cnt.keys():
            res += cnt[x] * cnt[x ^ high] - cnt[x] * cnt[x ^ low]
        for _ in range(high_bit):
            nex = collections.Counter()
            for x in cnt.keys():
                if high & 1 == 1:
                    res += cnt[x] * cnt[x ^ (high - 1)]
                if low & 1 == 1:
                    res -= cnt[x] * cnt[x ^ (low - 1)]
                nex[x >> 1] += cnt[x]
            high = high >> 1
            low = low >> 1
            cnt = nex
        return res // 2
