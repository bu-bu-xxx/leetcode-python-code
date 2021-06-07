# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 用队列
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        import collections
        result = []
        queue = collections.deque([root])
        # 出队列时再读数值
        while queue:
            add_result = collections.deque()
            for _ in range(len(queue)):
                temp = queue.popleft()
                if temp is not None:
                    add_result.append(temp.val)
                    queue.append(temp.left)
                    queue.append(temp.right)
            # 加入result
            result.append(list(add_result))

        # 去掉最后一个空数组
        return result[0:len(result) - 1]


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    root1 = ListToTree([3, 9, 20, None, None, 15, 7])
    print(try1.levelOrder(root1))
