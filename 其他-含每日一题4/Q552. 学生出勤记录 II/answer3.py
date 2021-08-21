# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，矩阵快速幂
# 把迭代的数据变成向量，用矩阵表示转移矩阵
# 则只用求矩阵的n次幂即可，再用快速幂算法
from typing import List


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, columns, temp = len(a), len(b[0]), len(b)
            c = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    for k in range(temp):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c

        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        ans = sum(res[0])
        return ans % MOD
