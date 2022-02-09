# encoding:utf-8
# @Author :ZQY


# 自己做，简单
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        for rectangle in rectangles:
            if min(rectangle) > max_len:
                max_len = min(rectangle)
                res = 0
            if max_len == min(rectangle):
                res += 1
        return res
