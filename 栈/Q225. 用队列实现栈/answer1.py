# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 栈：后进先出，队列：先进后出
# 一个队列实现
# 每次进栈，就把前面的都取出来，都进一次队列
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        begin_len = len(self.queue)
        self.queue.append(x)
        for i in range(begin_len):
            temp = self.queue.popleft()
            self.queue.append(temp)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return bool(not self.queue)


if __name__ == '__main__':
    try1 = MyStack()
    print(try1.empty())
