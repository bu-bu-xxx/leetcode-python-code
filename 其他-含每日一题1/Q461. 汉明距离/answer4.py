# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 提交答案里，内存最小的
# 同样是一行


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x ^ y)).count('1')
