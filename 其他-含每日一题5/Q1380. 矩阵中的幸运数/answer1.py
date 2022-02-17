# encoding:utf-8
# @Author :ZQY


# 自己做，简单题
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row = [max(l) for l in matrix]
        res = []
        for j in range(n):
            val = max([matrix[i][j] for i in range(m)])
            idx = [matrix[i][j] for i in range(m)].index(val)
            if min(matrix[idx]) == val:
                res.append(val)

        return res
