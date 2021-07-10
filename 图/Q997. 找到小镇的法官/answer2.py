# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，改进
# 出入度
import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        in_count = collections.Counter()
        out_count = collections.Counter()
        for i, j in trust:
            in_count[i] += 1
            out_count[j] += 1
        for key, val in out_count.items():
            if val == n - 1 and in_count[key] == 0:
                return key
        return -1
