# encoding:utf-8
# @Author :ZQY


class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(bin(num))-3+bin(num).count('1')
