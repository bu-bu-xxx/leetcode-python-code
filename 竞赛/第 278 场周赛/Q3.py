# encoding:utf-8
# @Author :ZQY


# 5994. 查找给定哈希值的子串
# 每算一次就要取一次mod啊啊啊


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        res = ""
        val = lambda ch: ord(ch) - ord('a') + 1

        tmp = 0
        for i in range(len(s) - k, len(s)):
            tmp += val(s[i]) * pow(power, i - len(s) + k, modulo)
            tmp %= modulo

        for end in range(len(s) - 1, k - 2, -1):
            beg = end - k + 1
            if tmp == hashValue:
                res = s[beg:end + 1]
            tmp = (tmp - val(s[end]) * pow(power, k - 1, modulo)) * power + val(s[beg - 1])
            tmp %= modulo
        return res
