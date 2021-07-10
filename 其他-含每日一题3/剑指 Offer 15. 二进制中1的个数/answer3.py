# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，位运算
# n&(n-1)，记录迭代次数


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res
