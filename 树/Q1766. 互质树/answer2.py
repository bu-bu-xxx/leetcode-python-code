# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 1 <= nums[i] <= 50
# 所以先存50以内的互质数，更快
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

        node_father = [-1] * len(nums)
        for edge in edges:
            node_father[max(edge)] = min(edge)
        nodes = {i for i in range(len(nums))}
        res = [-1] * len(nums)
        while nodes:
            node = nodes.pop()
            node_prime = prime[nums[node]]
            tmp = node
            while tmp != 0:
                tmp = node_father[tmp]
                if nums[tmp] in node_prime:
                    res[node] = tmp
                    break
        return res


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [5, 6, 10, 2, 3, 6, 15]
    edges1 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    print(try1.getCoprimes(nums1, edges1))
