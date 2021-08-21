# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# 0正常，1迟到，2翘课
import collections


class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        beg = ("00", 0)

        def nex_count(s):
            if s[1] == 0:
                if s[0] == "11":
                    return [("10", 0), ("12", 1)]
                else:
                    return [(s[0][-1] + "0", 0), (s[0][-1] + "1", 0), (s[0][-1] + "2", 1)]
            else:
                if s[0] == "11":
                    return [("10", 1)]
                else:
                    return [(s[0][-1] + "0", 1), (s[0][-1] + "1", 1)]

        dp = collections.Counter()
        dp[beg] += 1
        for _ in range(n):
            dp_nex = collections.Counter()
            for tmp in dp.keys():
                dp[tmp] = dp[tmp] % mod
                for nex in nex_count(tmp):
                    dp_nex[nex] += dp[tmp]
            dp = dp_nex

        return sum(dp.values()) % mod


if __name__ == "__main__":
    try1 = Solution()
    n1 = 75633
    print(try1.checkRecord(n1))
