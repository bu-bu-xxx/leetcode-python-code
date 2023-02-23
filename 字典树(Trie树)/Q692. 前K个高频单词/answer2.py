# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 优先队列
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = collections.Counter()
        for word in words:
            word_dict[word] += 1
        heap = [(-value, key) for key, value in word_dict.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
