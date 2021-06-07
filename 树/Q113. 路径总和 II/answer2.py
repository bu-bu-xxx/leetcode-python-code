# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 队列中存(当前节点，当前路径，路径和)
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        import collections
        if not root:
            return []

        queue = collections.deque()
        queue.append((root,[root.val],root.val))
        result = []
        while queue:
            temp = queue.popleft()
            if (t_left := temp[0].left) is not None:
                new = (t_left,temp[1]+[t_left.val],temp[2]+t_left.val)
                queue.append(new)
            if (t_right := temp[0].right) is not None:
                new = (t_right, temp[1]+[t_right.val], temp[2] + t_right.val)
                queue.append(new)
            if t_left is None and t_right is None and temp[2] == targetSum:
                result.append(temp[1])

        return result


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    null = None
    root1 = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    root1 = ListToTree(root1)
    targetSum1 = 22
    print(try1.pathSum(root1, targetSum1))
