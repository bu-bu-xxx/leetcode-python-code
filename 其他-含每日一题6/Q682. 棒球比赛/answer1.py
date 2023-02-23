# encoding:utf-8
# @Author :ZQY


# 自己做，easy题
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for val in ops:
            try:
                stack.append(int(val))
            except:
                if val == "+":
                    stack.append(stack[-1] + stack[-2])
                elif val == "D":
                    stack.append(stack[-1] * 2)
                else:
                    stack.pop()

        return sum(stack)
