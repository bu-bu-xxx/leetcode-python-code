# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
