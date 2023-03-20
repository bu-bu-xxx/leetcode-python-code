# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2536. 子矩阵元素加 第 337 场周赛
# 普通方法，复杂度太高
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        for row1,col1,row2,col2 in queries:
            for i in range(row1,row2+1):
                for j in range(col1,col2+1):
                    mat[i][j] += 1
        return mat
