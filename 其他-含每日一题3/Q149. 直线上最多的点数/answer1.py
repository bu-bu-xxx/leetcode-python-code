# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，暴力算法
# 每两个点的直线都求出来
# k = (y1-y2)/(x1-x2)
# b = (x2y1-x1y2)/(x1-x2)
import collections
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        count = collections.Counter()
        k = lambda x1, y1, x2, y2: (y1 - y2) / (x1 - x2) if x1 != x2 else float('inf')
        b = lambda x1, y1, x2, y2: (x2 * y1 - x1 * y2) / (x1 - x2) if x1 != x2 else x1
        for i, [x1, y1] in enumerate(points):
            for x2, y2 in points[i + 1:]:
                count[(k(x1, y1, x2, y2), b(x1, y1, x2, y2))] += 1
        res = max(count.values())
        return round((math.sqrt(1 + 8 * res) + 1) / 2)
