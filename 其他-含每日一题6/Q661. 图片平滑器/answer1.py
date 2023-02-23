# encoding:utf-8
# @Author :ZQY


# 自己做
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        direction = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum_val = img[i][j]
                col = 1
                for i_add, j_add in direction:
                    if 0 <= i + i_add < m and 0 <= j + j_add < n:
                        sum_val += img[i + i_add][j + j_add]
                        col += 1
                res[i][j] = sum_val // col
        return res
