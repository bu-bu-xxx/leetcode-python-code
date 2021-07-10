# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Q1
# 5784. 重新分配字符使所有字符串都相等
import collections
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = collections.Counter()
        for word in words:
            for s in word:
                count[s] += 1

        for val in count.values():
            if val % n != 0:
                return False
        return True
