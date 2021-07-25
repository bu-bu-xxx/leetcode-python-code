# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，冲冲冲
# ez题目


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pre = set()
        res = 0
        for ch in s:
            if ch not in pre:
                pre.add(ch)
            else:
                pre -= {ch}
                res += 2
        if len(pre) >= 1:
            return res + 1
        return res
