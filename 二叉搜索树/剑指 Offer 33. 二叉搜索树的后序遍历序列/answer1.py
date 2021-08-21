# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，辅助单调栈+前序遍历分析
# 算法流程：
# 1.倒序遍历，变成对称的前序遍历
# 2.1. check if new>root False
# 2.2. if new>peek 入栈
# 2.3. if new<peek , 循环出栈找到最小的root>new(直到栈空) , 入栈new
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        postorder = postorder[-1::-1]
        root = float('inf')
        stack = [float('-inf')]

        for new in postorder:
            if new > root:
                return False
            if new < stack[-1]:
                while stack[-1] > new:
                    root = stack[-1]
                    stack.pop()
            stack.append(new)

        return True
