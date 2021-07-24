# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，排序题目
# 用sorted，ez
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        res = len(citations)
        for val in citations:
            if val >= res:
                return res
            res -= 1
        return 0
