# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，暴力穷举
# 穷举左上角坐标和右下角坐标
# 不出所料，超时了
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        for x1 in range(m):
            for y1 in range(n):
                for x2 in range(x1, m):
                    for y2 in range(y1, n):
                        if sum(sum([k[y1:y2 + 1] for k in matrix[x1:x2 + 1]], [])) \
                                == target:
                            result += 1
        return result


if __name__ == "__main__":
    try1 = Solution()
    matrix1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target1 = 0
    print(try1.numSubmatrixSumTarget(matrix1, target1))
