# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 记录每个点的父节点
# 然后暴力搜索每一个点
from math import gcd
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        node_father = [-1] * len(nums)
        for edge in edges:
            node_father[max(edge)] = min(edge)
        nodes = {i for i in range(len(nums))}
        res = [-1] * len(nums)
        while nodes:
            node = nodes.pop()
            tmp = node
            while tmp != 0:
                tmp = node_father[tmp]
                if gcd(nums[node], nums[tmp]) == 1:
                    res[node] = tmp
                    break
        return res


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [5, 6, 10, 2, 3, 6, 15]
    edges1 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    print(try1.getCoprimes(nums1, edges1))
