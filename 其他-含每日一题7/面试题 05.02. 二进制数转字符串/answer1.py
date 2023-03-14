# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
import fractions
import re


class Solution:
    def printBin(self, num: float) -> str:
        n = len(str(num)) - 2
        tmp = fractions.Fraction(int(str(num)[2:]), 10 ** n)
        [a, b] = re.findall(r'[0-9]+', str(tmp))
        a, b = int(a), int(b)

        b_pow = 0
        while b > 1:
            if b % 2 == 1:
                return "ERROR"
            b //= 2
            b_pow += 1

        tmp = bin(a)[2:]
        return "0." + "0" * (b_pow - len(tmp)) + tmp
