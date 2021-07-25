# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，贪心
# 直到找到适合的饼干为止
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g = sorted(g)
        s = sorted(s)
        for ss in s:
            if res < len(g) and g[res] <= ss:
                res += 1
        return res
