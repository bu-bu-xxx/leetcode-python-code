# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，并查集
# 初始每个点属于不同连通分量
# 每读取一条边，如果两个点属于不同连通分量，则合并
# 如果属于同一个连通分量，则形成环，输出这个边即可
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num = len(edges)
        record = list(range(num + 1))

        # 找到同一个连通分量的最小节点
        def find(node: int) -> int:
            if node != record[node]:
                return find(record[node])
            return node

        for edge in edges:
            if (root0 := find(edge[0])) != (root1 := find(edge[1])):
                record[root1] = root0
            else:
                return edge
