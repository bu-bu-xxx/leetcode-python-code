# encoding:utf-8
# @Author :ZQY


# 自己做，冲冲冲
import collections
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word1, word2 = s1.split(' '), s2.split(' ')
        count = collections.Counter()
        for t in word1:
            count[t] += 1
        for t in word2:
            count[t] += 1

        res = list()
        for key,value in count.items():
            if value == 1:
                res.append(key)

        return res








