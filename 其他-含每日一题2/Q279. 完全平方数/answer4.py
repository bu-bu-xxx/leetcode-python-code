# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 参考官方答案的评论，广度优先搜索
# 用到一个定理，一个正整数最少由小于等于4个平方数和组成
# 先测n是不是平方数，然后把差入栈，直到找到平方数
import collections
import math


class Solution:
    def numSquares(self, n: int) -> int:
        nums = [s ** 2 for s in range(1, math.floor(n ** 0.5) + 1)]
        queue = collections.deque([n])
        for count in range(1, 4):
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp in nums:
                    return count
                for num in nums:
                    if tmp > num:
                        queue.append(tmp - num)
                    else:
                        break
        return 4
