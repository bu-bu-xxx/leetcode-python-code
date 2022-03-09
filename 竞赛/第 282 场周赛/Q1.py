# encoding:utf-8
# @Author :ZQY


# 2185. 统计包含给定前缀的字符串
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) >= len(pref) and word[0:len(pref)] == pref:
                res += 1
        return res
