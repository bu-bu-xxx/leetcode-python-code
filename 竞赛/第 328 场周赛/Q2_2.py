# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2536. 子矩阵元素加 1
# 二维差分，即两次一维差分，降低复杂度
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            mat[row2][col2] += 1
            if row1 - 1 >= 0:
                mat[row1 - 1][col2] -= 1
            if col1 - 1 >= 0:
                mat[row2][col1 - 1] -= 1
            if row1 - 1 >= 0 and col1 - 1 >= 0:
                mat[row1 - 1][col1 - 1] += 1

        for i in range(n):
            tmp = 0
            for j in range(n - 1, -1, -1):
                mat[i][j] += tmp
                tmp = mat[i][j]

        for j in range(n):
            tmp = 0
            for i in range(n - 1, -1, -1):
                mat[i][j] += tmp
                tmp = mat[i][j]

        return mat
