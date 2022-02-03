# encoding:utf-8
# @Author :ZQY


# 参考了官方答案
# 二进制，枚举


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << ord(s[j]) - ord('a')
                else:
                    upper |= 1 << ord(s[j]) - ord('A')
                if len(res) < (j - i + 1) and lower == upper:
                    res = s[i:j + 1]

        return res
