# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，贪心算法


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(st: str):
            n = len(st)
            for i in range(n):
                if st[i] != st[n - 1 - i]:
                    return i
            return -1

        if (i := check(s)) == -1:
            return True
        if check(s[0:i] + s[i + 1:len(s)]) == -1:
            return True
        if check(s[0:len(s) - 1 - i] + s[len(s) - i:len(s)]) == -1:
            return True
        return False
