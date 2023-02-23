# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 数学
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        length = len(str(num))
        for i in range(length - 1):
            res += int(str(num)[i]) * 10 ** (length - i - 1) // 2
        for j in range(num // 10 * 10, num + 1):
            if sum([int(s) for s in list(str(j))]) % 2 - 1:
                res += 1
        return res - 1
