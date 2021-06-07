# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，对answer2的优化
# 由于dp[i][][]的每个元素值的计算只和dp[i−1][][]的元素值有关，
# 因此可以使用滚动数组的方式，去dp的第一个维度
# 实现时，内层循环需采用倒序遍历的方式，这种方式保证转移来的是dp[i−1][][]中的元素值
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 转移矩阵迭代
        for i in range(1, length + 1):
            zeros = strs[i - 1].count('0')
            ones = len(strs[i - 1]) - zeros
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)
        # 找最大值
        return dp[m][n]


if __name__ == '__main__':
    try1 = Solution()
    strs1 = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11",
             "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
    m1 = 100
    n1 = 200
    print(try1.findMaxForm(strs1, m1, n1))
