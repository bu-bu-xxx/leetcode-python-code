# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# 0正常，1迟到，2翘课
# dp[i][j]表示最后有i个迟到，共j个翘课
# answer1的改进版


class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7

        dp = [[0] * 2 for j in range(3)]
        dp[0][0] = 1

        for _ in range(n):
            dp_nex = [[0] * 2 for j in range(3)]
            dp_nex[0][0] = (dp[0][0] + dp[1][0] + dp[2][0]) % mod
            dp_nex[1][0] = (dp[0][0]) % mod
            dp_nex[2][0] = (dp[1][0]) % mod
            dp_nex[0][1] = (dp[0][1] + dp[1][1] + dp[2][1] + dp[0][0] + dp[1][0] + dp[2][0]) % mod
            dp_nex[1][1] = (dp[0][1]) % mod
            dp_nex[2][1] = (dp[1][1]) % mod
            dp = dp_nex

        return sum(sum(dp, [])) % mod


if __name__ == "__main__":
    try1 = Solution()
    n1 = 10101
    print(try1.checkRecord(n1))
