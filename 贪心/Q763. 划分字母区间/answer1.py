# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，冲冲冲
# ez题目
import collections
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mem = collections.Counter()
        for i, ch in enumerate(s):
            mem[ch] = i

        end = 0
        count = 0
        res = []
        for start, ch in enumerate(s):
            end = max(mem[ch], end)
            count += 1
            if start == end:
                res.append(count)
                count = 0

        return res
