# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5816. 查询最大基因差
# 我写的这个不行，要用字典树(前缀树)
from typing import List


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for node,val in queries:
            ans = 0
            while parents[node] != -1:
                ans = max(ans,val^node)
                node = parents[node]
            ans = max(val^node,ans)
            res.append(ans)
        return res





