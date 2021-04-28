# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做的，栈
# 都进栈，碰到右括号，出栈直到左括号
# 按顺序计算，进栈最终值
# 所有都遍历一遍即为最终答案
# 从右往左读取s，倒着进栈

def cal_in(num1, cal, num2):
    num1 = int(num1)
    num2 = int(num2)
    dict_cal = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2
    }
    return dict_cal[cal](num1, num2)


class Solution:
    def calculate(self, s):
        stack = []
        s_sec = []
        # 把数字串变成数字
        temp = ''
        for i in s:
            if i == ' ':
                continue
            try:
                a = int(i)
                temp += i
            except:
                if temp != '':
                    s_sec.append(temp)
                if i == '(':
                    s_sec.append(i)
                    temp = '0'
                else:
                    s_sec.append(i)
                    temp = ''
        if temp != '':
            s_sec.append(temp)
        # 第一次遍历，计算括号内的数
        # 第一个是-，则加0
        if s[0]=='-':
            s = [0]
            s.extend(s_sec)
        else:
            s = s_sec

        s_len = len(s)
        for i in range(-1, -s_len - 1, -1):
            if s[i] != '(':
                stack.append(s[i])
                continue
            # 碰到左括号
            first = stack.pop()
            second = stack.pop()
            while second != ')':
                num1 = first
                cal = second
                num2 = stack.pop()
                stack.append(cal_in(num1, cal, num2))
                first = stack.pop()
                second = stack.pop()
            stack.append(first)

        # 当遍历完再算剩余的
        while len(stack) > 1:
            num1 = stack.pop()
            cal = stack.pop()
            num2 = stack.pop()
            stack.append(cal_in(num1, cal, num2))

        return int(stack[0])


if __name__ == "__main__":
    try1 = Solution()

    s = "-2+ 1"
    print(try1.calculate(s))
