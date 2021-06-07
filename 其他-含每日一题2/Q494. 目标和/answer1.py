# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# dp矩阵为转移矩阵，dp[i][j]表示前i个数字凑成j的数量
# sum_max = sum(nums[i])
# dp[i][j] = dp[i-1][j-num] if j>-num+sum_max
#          = dp[i-1][j+num] if j<num-sum_max
#          = dp[i-1][j-num] + dp[i-1][j+num] else
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_max = sum(nums)
        if target > sum_max or target < -sum_max:
            return 0
        dp = [[0 for _ in range(2 * sum_max + 1)] for _ in range(len(nums))]
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(-sum_max, sum_max + 1):
                if j > -num + sum_max:
                    dp[i][j] = dp[i - 1][j - num]
                elif j < num - sum_max:
                    dp[i][j] = dp[i - 1][j + num]
                else:
                    dp[i][j] = dp[i - 1][j - num] + dp[i - 1][j + num]
        return dp[len(nums) - 1][target]


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(try1.findTargetSumWays(nums1, target1))
