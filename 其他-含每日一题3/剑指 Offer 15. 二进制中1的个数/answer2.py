# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，位运算


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res
