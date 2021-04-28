# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = 10**6

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None

        self.min_val = 10 ** 10
        for i in self.stack:
            self.min_val = min(self.min_val, i)
        return self.min_val


if __name__ == '__main__':
    minStack = MinStack()

    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
