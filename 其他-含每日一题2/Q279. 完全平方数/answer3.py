# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 参考官方答案的评论，贪心算法
# 用到一个定理，一个正整数最少由小于等于4个平方数和组成
# 每次搜索该整数由1个2个3个组成
import math


class Solution:
    def numSquares(self, n: int) -> int:
        nums = [s ** 2 for s in range(1, math.floor(n ** 0.5) + 1)]

        def check(num, count):
            if count == 1:
                return num in nums
            else:
                for s in nums:
                    if num > s and check(num - s, count - 1):
                        return True
                return False

        for c in range(1, 4):
            if check(n, c):
                return c
        return 4
