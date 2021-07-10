# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，并查集
# 把情侣偶数连到奇数
# 把连续两个座位作为点，画图
# 并查集合并，集合长度-1为换座位次数
import collections
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        edges = [[] for _ in range(n)]
        state = list(range(n))
        for i in range(2 * n):
            cp = row[i] // 2
            node = i // 2
            edges[cp].append(node)

        class union:
            def find(self, nd):
                if state[nd] == nd:
                    return nd
                state[nd] = self.find(state[nd])
                return state[nd]

            def merge(self, nd1, nd2):
                state[self.find(nd2)] = self.find(nd1)

        un = union()
        for i, j in edges:
            un.merge(i, j)
        count = collections.Counter()

        for i in range(n):
            count[un.find(i)] += 1
        res = 0
        for key, val in count.items():
            res += val - 1
        return res
