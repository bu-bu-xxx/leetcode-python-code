# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，广度优先遍历+位运算
# queue存每一种可能
import collections
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        queue = collections.deque()
        queue.append(0)

        for s in arr:
            s_val = 0
            for ch in s:
                if (s_val >> (ord(ch) - ord("a"))) & 1 == 1:
                    s_val = 0
                    break
                else:
                    s_val |= 1 << (ord(ch) - ord("a"))
            if s_val == 0:
                continue

            for _ in range(len(queue)):
                tmp = queue.popleft()
                queue.append(tmp)
                if tmp & s_val == 0:
                    queue.append(tmp | s_val)

        return max([bin(s).count("1") for s in queue])
