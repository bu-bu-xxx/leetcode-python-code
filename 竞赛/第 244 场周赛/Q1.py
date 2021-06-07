# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Q1
# 5776. 判断矩阵经轮转后是否一致
import re,collections,math
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotation(m):
            n_len = len(m)
            n = [0]*n_len
            for i in range(n_len):
                n[i] = [k[i] for k in m[-1::-1]]
            return n

        for _ in range(4):
            if (tmp := rotation(mat)) == target:
                return True
            mat = tmp
        return False







