# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 逆波兰算法：把算式中序遍历转换成后序遍历
# 本题用后序遍历算出答案

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calculation(num1, num2, i))
        return stack[0]


def calculation(num1, num2, i):
    cal_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }
    return cal_dict[i](num1, num2)


if __name__ == '__main__':
    try1 = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    print(try1.evalRPN(tokens))
