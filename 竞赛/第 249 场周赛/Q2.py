# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5809. 长度为 3 的不同回文子序列
import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        record = collections.defaultdict(list)
        for i,ch in enumerate(s):
            if not record[ch]:
                record[ch].append(i)
            elif len(record[ch]) == 1:
                record[ch].append(i)
            else:
                record[ch][1] = i

        res = 0
        for key,val in record.items():
            if len(val) == 2:
                tmp = set(s[val[0]+1:val[1]])
                res+=len(tmp)

        return res






