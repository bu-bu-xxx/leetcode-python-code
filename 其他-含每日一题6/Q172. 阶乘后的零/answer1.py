# encoding:utf-8
# @Author :ZQY


# 自己做，数学
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0

        while n > 0:
            n //= 5
            res += n
        return res

