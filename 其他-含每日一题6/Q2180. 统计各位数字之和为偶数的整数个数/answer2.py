# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 暴力枚举
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            if sum([int(s) for s in list(str(i))]) % 2 == 0:
                res += 1
        return res
