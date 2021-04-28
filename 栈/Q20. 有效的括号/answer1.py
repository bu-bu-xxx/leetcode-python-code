# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 栈stack，右进右出
# list append最后位置添加元素。pop删除一个位置的元素，默认最后一个
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['?']
        dict1 = {'(': ')', '[': ']', '{': '}', '?': '?'}
        for ch in s:
            if ch in dict1:
                stack.append(ch)
            elif dict1[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    try1 = Solution()

    s = '()'
    print(try1.isValid(s))
