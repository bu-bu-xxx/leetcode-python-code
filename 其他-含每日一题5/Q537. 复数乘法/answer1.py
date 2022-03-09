# encoding:utf-8
# @Author :ZQY


# 自己做，so easy
import re


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        [a1, b1] = re.findall(r'[^\+^i]+', num1)
        [a2, b2] = re.findall(r'[^\+^i]+', num2)
        a1, b1, a2, b2 = int(a1), int(b1), int(a2), int(b2)
        a3, b3 = a1 * a2 - b1 * b2, a1 * b2 + a2 * b1
        return str(a3) + '+' + str(b3) + 'i'
