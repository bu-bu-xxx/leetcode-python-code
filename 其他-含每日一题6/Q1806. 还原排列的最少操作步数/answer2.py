# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 数学法
# 最少φ(n)次
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        res = 0
        mod = 1
        for i in range(n):
            res += 1
            mod = mod * 2 % (n - 1)
            if mod == 1:
                return res
