# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 栈
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if i == '..' and not stack:
                stack = stack
            elif i == '..':
                stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    try1 = Solution()

    s = '/home/'
    print(try1.simplifyPath(s))
