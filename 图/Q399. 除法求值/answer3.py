# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 其他答案，Floyd算法
# 每次查询A到B经过k的最短路径
# for k，for A，for B，最后得到A到B经过任意点的最短距离
# 时间复杂度:O(n^3)；空间复杂度:O(n^2)
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        road = dict()
        node_set = set()
        for [a, b], val in zip(equations, values):
            road[(a, b)] = val
            road[(b, a)] = 1 / val
            node_set |= {a, b}

        # Floyd算法
        for k in node_set:
            for i in node_set:
                for j in node_set:
                    if (i, k) in road and (k, j) in road:
                        road[(i, j)] = road[(i, k)] * road[(k, j)]

        # 回答问题
        res = []
        for a, b in queries:
            if a in node_set and b in node_set and (a, b) in road:
                res.append(road[(a, b)])
            else:
                res.append(-1)
        return res
