# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单排序
import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = collections.Counter()
        for word in words:
            word_dict[word] += 1
        word_list = []
        for word in words:  # enumerate 枚举
            if word_dict[word] != 0:
                word_list.append((-word_dict[word],word))
                word_dict[word] = 0
        word_list = sorted(word_list)
        return [word_list[i][1] for i in range(k)]

