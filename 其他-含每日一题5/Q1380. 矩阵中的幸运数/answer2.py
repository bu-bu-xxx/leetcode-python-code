# encoding:utf-8
# @Author :ZQY


# 自己做
import collections
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        count = collections.Counter()
        for tmp in [min(l) for l in matrix]:
            count[tmp] += 1
        for tmp in [max([matrix[i][j] for i in range(len(matrix))]) for j in range(len(matrix[0]))]:
            count[tmp] += 1
        return [val for val, num in count.items() if num >= 2]
