# encoding:utf-8
# @Author :ZQY


# 2186. 使两字符串互为字母异位词的最少步骤数
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter()
        count_t = collections.Counter()
        for ch in s:
            count_s[ch] += 1
        for ch in t:
            count_t[ch] += 1
        return sum([abs(count_s[chr(i)] - count_t[chr(i)]) for i in range(ord('a'), ord('z') + 1)])
