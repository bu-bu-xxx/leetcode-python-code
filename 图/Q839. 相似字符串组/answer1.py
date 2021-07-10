# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，并查集
import collections
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        state = list(range(n))

        def check(s1: str, s2: str) -> bool:
            count = 0
            for i in range(m):
                if s1[i] != s2[i]:
                    count += 1
            return count <= 2

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
                if check(strs[i], strs[j]):
                    merge(i, j)

        col = collections.Counter()
        for i in range(n):
            col[find(i)] += 1
        return len(col.keys())
