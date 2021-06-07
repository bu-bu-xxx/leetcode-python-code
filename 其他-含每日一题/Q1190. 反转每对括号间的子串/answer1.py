# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，栈
# 按栈存
# 当发现右边括号，就出栈，并发过来，直到左括号
# 如果出完栈非空，则按从左到右顺序入栈


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                temp = ""
                while (a := stack.pop()) != '(':
                    temp += a
                else:
                    for j in temp:
                        stack.append(j)

        return ''.join(stack)


if __name__ == "__main__":
    try1 = Solution()
    s1 = "(abcd)"
    print(try1.reverseParentheses(s1))
