# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        n = len(s) // (2 * k)
        for i in range(n + 1):
            res += s[(i * 2 * k):(i * 2 * k + k)][-1::-1]
            res += s[(i * 2 * k + k):(i * 2 * k + 2 * k)]

        return res
