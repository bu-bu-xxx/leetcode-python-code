# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 别人的迭代
# 我的时间空间复杂度均是别人的十倍
# 每次存对称的两个点，比如左节点左孩子，右节点右孩子
# 每次pop两个点
# 可以看成每次操作都是左半边加右半边对称点
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        # 构建queue
        import collections
        queue = collections.deque([root.left,root.right])

        # 迭代
        while queue:
            temp1 = queue.popleft()
            temp2 = queue.popleft()
            # 判断是否相同
            if temp1 is None and temp2 is None:
                continue
            if temp1 is None or temp2 is None:
                return False
            if temp1.val != temp2.val:
                return False
            # 当前点相同，并且都有值，则存入下一对点
            queue.append(temp1.left)
            queue.append(temp2.right)
            queue.append(temp1.right)
            queue.append(temp2.left)

        return True
