# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单


class Solution:
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 1:
                return False
            n //= 2
        return True
