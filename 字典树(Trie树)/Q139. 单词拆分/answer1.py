# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 哈希表，动态规划
import collections
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = collections.Counter(wordDict)
        table = [1] + [0] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if table[j] == 1 and s[j:i] in word_dict:
                    table[i] = 1
        return table[-1] == 1
