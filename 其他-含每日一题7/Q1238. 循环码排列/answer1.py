# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        rec_set = set()
        res = [start]
        rec_set.add(start)
        now = start

        for _ in range(2 ** n - 1):
            for i in range(n):
                if (nex := (2 ** i) ^ now) not in rec_set:
                    res.append(nex)
                    rec_set.add(nex)
                    now = nex
                    break

        return res
