# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，ez
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mem = []
        for i, val in enumerate(mat):
            mem.append((sum(val), i))

        mem = sorted(mem)
        res = [s[1] for s in mem[:k]]
        return res
