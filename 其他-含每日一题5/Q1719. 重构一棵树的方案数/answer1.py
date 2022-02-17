# encoding:utf-8
# @Author :ZQY


# 参考了官方答案
# 只需要对每个pair讨论是否有祖先后代关系即可
# 即degree(A)<=degree(B),adj(A)⊆adj(B)是否对于任意(A,B)∈pairs成立
# 且要有一个根节点
import collections
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = collections.defaultdict(set)

        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
        for key in adj.keys():
            adj[key].add(key)

        # 是否有根节点
        if max([len(val) for val in adj.values()]) != len(adj.keys()):
            return 0

        record = 1  # 记录是否有degree相同的点
        for a, b in pairs:
            if len(adj[a]) <= len(adj[b]):
                if not adj[a].issubset(adj[b]):
                    return 0
            else:
                if not adj[b].issubset(adj[a]):
                    return 0
            if len(adj[a]) == len(adj[b]):
                record = 2

        return record


if __name__ == "__main__":
    try1 = Solution()
    pairs = [[1, 2], [2, 3]]
    print(try1.checkWays(pairs))
