# encoding:utf-8
# @Author :ZQY


# 5300. 有向无环图中一个节点的所有祖先
import collections
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestor = collections.defaultdict(set)
        parents = collections.defaultdict(list)
        for u, v in edges:
            parents[v].append(u)

        def dfs(node):
            if ancestor[node]:
                return ancestor[node]
            for p_node in parents[node]:
                ancestor[node] |= dfs(p_node)
                ancestor[node].add(p_node)
            return ancestor[node]

        for i in range(n):
            dfs(i)

        return [sorted(list(ancestor[i])) for i in range(n)]
