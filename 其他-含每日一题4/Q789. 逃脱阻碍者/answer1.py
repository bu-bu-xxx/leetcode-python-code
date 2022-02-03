# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单数学
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(point1:List[int],point2:List[int]):
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
        limit = distance(target,[0,0])
        for ghost_point in ghosts:
            if distance(ghost_point,target) <= limit:
                return False
        return True






