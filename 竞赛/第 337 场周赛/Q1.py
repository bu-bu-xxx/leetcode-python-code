# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6319. 奇偶位数
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n = bin(n)[2:][-1::-1]
        res = [0, 0]
        for i in range(len(n)):
            if i % 2 == 1 and n[i] == "1":
                res[1] += 1
            if i % 2 == 0 and n[i] == "1":
                res[0] += 1
        return res
