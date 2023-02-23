# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 字典树
from typing import List

high_bit = 15


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, x: int):
        node = self.root
        for i in range(high_bit - 1, -1, -1):
            x_bit = (x >> i) & 1
            if not node.children[x_bit]:
                node.children[x_bit] = TrieNode()
            node = node.children[x_bit]
            node.sum += 1

    def get(self, x: int, t: int):
        node = self.root
        res = 0
        for i in range(high_bit - 1, -1, -1):
            x_bit = (x >> i) & 1
            t_bit = (t >> i) & 1
            if t_bit:
                if node.children[x_bit ^ 0]:
                    res += node.children[x_bit ^ 0].sum
                if node.children[x_bit ^ 1]:
                    node = node.children[x_bit ^ 1]
                else:
                    return res
            else:
                if node.children[x_bit ^ 0]:
                    node = node.children[x_bit ^ 0]
                else:
                    return res

        res += node.sum
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        Trie1 = Trie()
        for num in nums:
            Trie1.add(num)

        res = 0
        for num in nums:
            res += Trie1.get(num, high)
            res -= Trie1.get(num, low - 1)

        return res // 2


if __name__ == "__main__":
    nums = [1, 4, 2, 7]
    low = 2
    high = 6
    try1 = Solution()
    print(try1.countPairs(nums, low, high))
