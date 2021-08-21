# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，贪心算法
# 把气球右端升序排列，可证明只需考虑只从右端射箭
# 每次选最小的右端值射箭，可证明如果射后面的，则前面的一定不会被射到
# 当这一箭在第j个气球停下，则从第j个气球射第二箭
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda s: s[1])
        now = float('-inf')
        res = 0
        for lt, rt in points:
            if now < lt:
                now = rt
                res += 1

        return res
