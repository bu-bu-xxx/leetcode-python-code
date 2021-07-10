# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 标记0为未搜索，1为A集合，-1为B集合
# 然后搜索完全部点，标记
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        tag = [0] * n
        res = [True]

        # 输入当前点和正确的belong
        def dfs(node, bl):
            for nex in graph[node]:
                if res[0] is False:
                    return
                if tag[nex] == 0:
                    tag[nex] = bl * (-1)
                    dfs(nex, bl * (-1))
                elif tag[nex] != bl * (-1):
                    res[0] = False

        for i, val in enumerate(tag):
            if val == 0:
                tag[i] = 1
                dfs(i, 1)
                if res[0] is False:
                    return False
        return True


if __name__ == "__main__":
    try1 = Solution()
    graph1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(try1.isBipartite(graph1))
