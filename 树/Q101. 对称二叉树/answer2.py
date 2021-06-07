# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，迭代
# 用队列存，一个左出队列，一个右出队列
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp_val = [i.val if i else None for i in queue]
            if collections.Counter(temp_val)[None] == len(temp_val):
                return True
            if temp_val != temp_val[-1::-1]:
                return False
            for _ in range(len(queue)):
                temp = queue.popleft()
                if temp:
                    queue.append(temp.left)
                    queue.append(temp.right)
                else:
                    queue.append(None)
                    queue.append(None)


if __name__ == '__main__':
    try1 = Solution()

    from 树.TreeNode.TreeNode import ListToTree

    root1 = ListToTree([1, 2, 2, 3, 4, 4, 3])
    print(try1.isSymmetric(root1))
