# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 别人的高分答案，尝试
# 一行


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
