# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 每次遍历的点存起来
# 如果发现遍历的点已经存过，则有环
# 然后存这个递归链上的所有边，返回重复的节点
# 两个节点中间的是环上的边
import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = collections.defaultdict(list)
        rec = dict()
        for i, edge in enumerate(edges):
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            rec[str(edge)] = i

        # 深度优先搜索
        search = [1] + [0] * n
        find_edges = []

        def dfs(node, father):
            search[node] = 1
            for nex in graph[node]:
                if nex != father:
                    if search[nex] == 0:
                        a = dfs(nex, node)
                        if a:
                            find_edges.append(sorted([nex, node]))
                            return a
                    else:
                        find_edges.append(sorted([nex, node]))
                        return nex

        # 找最后出现的边
        find_node = dfs(1, -1)
        for i, edge in enumerate(find_edges[1:]):
            if find_node in edge:
                find_edges = find_edges[0:i + 2]
                break
        return max(find_edges, key=lambda s: rec[str(s)])


if __name__ == "__main__":
    try1 = Solution()
    edges1 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(try1.findRedundantConnection(edges1))
