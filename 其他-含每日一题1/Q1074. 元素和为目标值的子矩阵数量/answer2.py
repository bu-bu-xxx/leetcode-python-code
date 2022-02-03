# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二维转一维，前缀和+哈希表
# 先遍历x1，x2，确定行坐标以后求和，得到关于列坐标的一维数组
# 求一维数组中和为target的子数组
# 遍历一维数组，用哈希表存前缀和，判断cur-target == pre，计数
from typing import List
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0

        # 一维数组target数量
        def countSubmatrix(sub: List[int]):
            pre = collections.Counter([0])
            ans = 0
            cur = 0
            for num in sub:
                cur += num
                if (cur - target) in pre:
                    ans += pre[cur - target]
                pre[cur] += 1
            return ans

        # 遍历每一行
        for i in range(m):
            submatrix = [0] * n
            for j in range(i, m):
                submatrix = [submatrix[k] + matrix[j][k] for k in range(n)]
                # 求一维数组的target值数量
                result += countSubmatrix(submatrix)

        return result


if __name__ == "__main__":
    try1 = Solution()
    matrix1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target1 = 0
    print(try1.numSubmatrixSumTarget(matrix1, target1))
