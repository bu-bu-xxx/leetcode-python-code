# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 用深度优先搜索试一下
# 添加一个高度函数depth = [-1]*len(nums)
# 数值u在当前搜索路径下的高度为depth[u]，stack[depth[u]]对应最近的这个值的坐标
# 这样只用遍历prime[u].length次，不用遍历至多50次


from math import gcd
from typing import List
import collections


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # 互质数
        prime = collections.defaultdict(set)
        for i in range(1, 51):
            for j in range(i, 51):
                if gcd(i, j) == 1:
                    prime[i].add(j)
                    prime[j].add(i)

        # 构建无向图连接表
        graph = collections.defaultdict(set)
        for [i, j] in edges:
            graph[i].add(j)
            graph[j].add(i)

        # 深度优先搜索
        stack = []  # 存当前路径的点坐标
        res = [-1] * len(nums)
        depth = [-1] * 51

        def dfs(father, node):
            index = -1
            for u in prime[nums[node]]:
                index = max(index, depth[u])
            if index != -1:
                res[node] = stack[index]
            tmp = depth[nums[node]]
            depth[nums[node]] = len(stack)
            stack.append(node)
            for nex in graph[node] - {father}:
                dfs(node, nex)
            stack.pop()
            depth[nums[node]] = tmp

        dfs(-1, 0)
        return res


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [5, 6, 10, 2, 3, 6, 15]
    edges1 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    print(try1.getCoprimes(nums1, edges1))
