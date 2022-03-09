# encoding:utf-8
# @Author :ZQY


# 2187. 完成旅途的最少时间
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def evaluate(t):
            return sum([t // t0 for t0 in time])

        def bi_method(beg, end):
            if beg == end:
                return beg
            mid = (beg + end) // 2
            if evaluate(mid) >= totalTrips:
                return bi_method(beg, mid)
            else:
                return bi_method(mid + 1, end)

        return bi_method(0, min(time) * totalTrips)
