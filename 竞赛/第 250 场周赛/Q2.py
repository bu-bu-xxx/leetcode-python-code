# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5814. 新增的最少台阶数
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pre = 0
        res = 0
        for rung in rungs:
            res += (rung - pre - 1) // dist
            pre = rung

        return res
