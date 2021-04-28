# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 迭代法

# next就是pop出一个数
# hanNext就是看stack和root是否为空

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.root = root

    def stack_func(self):
        while self.root or self.stack:
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            temp = self.stack.pop()
            self.root = temp.right
            return temp.val

    def next(self) -> int:
        return self.stack_func()

    def hasNext(self) -> bool:
        return bool(self.stack or self.root)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root9 = TreeNode(9)
    root20 = TreeNode(20)
    root15 = TreeNode(15, root9, root20)
    root3 = TreeNode(3)
    root7 = TreeNode(7, root3, root15)

    try1 = BSTIterator(root7)
    print(try1.next())
    print(try1.next())
    print(try1.hasNext())
