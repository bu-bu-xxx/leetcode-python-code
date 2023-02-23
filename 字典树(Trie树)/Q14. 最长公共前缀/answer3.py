# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 字典树
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.sum = 0

    def add(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
            node.sum += 1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie()
        for word in strs:
            root.add(word)

        node = root
        tmp = 0
        strs_len = len(strs)
        while strs_len in [s.sum for s in node.children if s]:
            tmp += 1
            for s in node.children:
                if s and s.sum == strs_len:
                    node = s
        return strs[0][0:tmp]
