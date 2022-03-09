# encoding:utf-8
# @Author :ZQY


# 5237. 得到回文串的最少操作次数
# 看了官方答案，用贪心算法，其实不难想到的，可惜
import collections


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        res = 0

        def move(s0: str):
            nonlocal res
            n = len(s0)
            if s0.count(s0[0]) > 1:
                times = s0[-1::-1].index(s0[0])
                end = n - 1 - times
                s0 = s0[:end] + s0[end + 1:] + s0[end]
                res += times
                return s0[1:n - 1]
            else:
                return move(s0[-1::-1])

        while len(s) > 1:
            s = move(s)

        return res
