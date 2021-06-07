# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，三维动态规划，背包问题
# 定义三维数组dp，其中dp[i][j][k]表示在前i个字符串中，
# 使用不超过j个0和k个1的情况下最多可以得到的字符串数量，
# 假设数组str的长度为l，则最终答案为dp[l][m][n]
# 备注：不超过j和k个的原因是，i=0时已经包括了浪费的0和1的个数
# 转移函数：
# dp[i][j][k] = 0 if i == 0
#             = dp[i-1][j][k] if i>0 and (j<zeros or k<ones)
#             = max(dp[i-1][j][k],dp[i-1][j-zeros][k-ones]+1) else
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(length + 1)]
        # 转移矩阵迭代
        for i in range(1, length + 1):
            zeros = strs[i-1].count('0')
            ones = len(strs[i - 1]) - zeros
            for j in range(m + 1):
                for k in range(n + 1):
                    if j < zeros or k < ones:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
        # 找最大值
        return max(sum(dp[length], []))


if __name__ == '__main__':
    try1 = Solution()
    strs1 = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11",
             "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
    m1 = 9
    n1 = 80
    print(try1.findMaxForm(strs1, m1, n1))
