# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 找到一个新的连接则少一个省份
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        searched = [0] * n
        res = n

        def dfs(now):
            nonlocal res
            searched[now] = 1
            for nex, v in enumerate(isConnected[now]):
                if v == 1 and searched[nex] == 0:
                    res -= 1
                    dfs(nex)

        for i, val in enumerate(searched):
            if val == 0:
                dfs(i)

        return res
