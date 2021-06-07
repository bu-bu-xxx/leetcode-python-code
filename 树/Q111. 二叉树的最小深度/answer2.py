# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 用队列，记录当前层数
# 当左右节点都不存在，则返回此时层数值
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        import collections
        queue = collections.deque()
        queue.append(root)
        now_deep = 0
        min_deep = float('inf')
        while queue:
            now_deep += 1
            for _ in range(len(queue)):
                temp = queue.popleft()
                if not temp:
                    continue
                # 如果是叶子节点
                if temp.left is None and temp.right is None:
                    min_deep = min(min_deep, now_deep)
                # 如果不是叶子
                queue.append(temp.left)
                queue.append(temp.right)

        return min_deep


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, ListToTree

    try1 = Solution()
    root1 = [3, 9, 20, None, None, 15, 7]
    root1 = ListToTree(root1)
    print(try1.minDepth(root1))
