# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，回溯
import collections
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        count = collections.Counter()
        for ch in s:
            count[ch] += 1
        cur = ""
        res = []
        n = len(s)

        def dfs(now: str):
            nonlocal cur
            cur += now
            if len(cur) == n:
                res.append(cur)
            for nex in count.keys():
                if count[nex] >= 1:
                    count[nex] -= 1
                    dfs(nex)
            cur = cur[:-1]
            count[now] += 1

        dfs("")
        return res
