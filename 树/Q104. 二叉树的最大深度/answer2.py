# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，广度优先搜索
# 一层一层遍历
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        import collections

        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        result = 0
        while queue:
            result += 1
            for _ in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return result
