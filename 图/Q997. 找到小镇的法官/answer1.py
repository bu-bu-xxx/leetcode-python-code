# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单
# 找出被信任人数为n-1即可
import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        count = collections.Counter()
        for i, j in trust:
            count[j] += 1
        res = []
        for name, val in count.items():
            if val == n - 1:
                res.append(name)
        if len(res) != 1:
            return -1
        else:
            for check, _ in trust:
                if check == res[0]:
                    return -1
            return res[0]
