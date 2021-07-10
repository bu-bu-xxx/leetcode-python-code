# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，并查集
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        state = list(range(n))

        def find(node):
            if state[node] == node:
                return node
            state[node] = find(state[node])
            return state[node]

        def merge(node1, node2):
            root1, root2 = find(node1), find(node2)
            state[root2] = root1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    merge(i, j)

        province = set()
        for city in range(n):
            province.add(find(city))

        return len(province)
