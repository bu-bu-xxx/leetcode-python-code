# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2575. 找出字符串的可整除数组
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        div = []
        pre = 0
        for a in word:
            pre = (pre * 10 + int(a)) % m
            if pre:
                div.append(0)
            else:
                div.append(1)
        return div
