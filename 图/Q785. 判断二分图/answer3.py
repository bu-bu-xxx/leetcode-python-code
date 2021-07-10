# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 找环路，环路上有奇数个点则不能分
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        tag = [0] * n
        rec = [True]

        def dfs(node, step):
            tag[node] = step
            for nex in graph[node]:
                if rec[0] is False:
                    return
                if tag[nex] == 0:
                    dfs(nex, step + 1)
                elif (step - tag[nex]) % 2 == 0:
                    rec[0] = False

        for i, val in enumerate(tag):
            if val == 0:
                dfs(i, 1)
                if rec[0] is False:
                    return False
        return True
