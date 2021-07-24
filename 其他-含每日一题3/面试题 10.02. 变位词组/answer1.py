# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，冲冲冲
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        def count(st: str):
            res = [0] * 26
            for ch in st:
                res[ord(ch) - ord("a")] += 1
            return tuple(res)

        for s in strs:
            ans[count(s)].append(s)
        return list(ans.values())
