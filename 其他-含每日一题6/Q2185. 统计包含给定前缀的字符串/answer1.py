# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if word[0:len(pref)] == pref:
                res += 1
        return res
