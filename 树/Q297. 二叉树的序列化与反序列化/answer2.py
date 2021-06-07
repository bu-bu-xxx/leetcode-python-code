# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 这题意思是用任何方式存储一个二叉树，为字符串
# 然后能把字符串转化为二叉树
# 用先序遍历
# 序列化：先序遍历，碰到None存入，然后return
# 反序列化：先一个把列表str转为TreeNode再进行序列化一样的步骤
from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'

        list_data = []

        def dfs(node):
            if node is None:
                list_data.append('null')
                return
            list_data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return '[' + ','.join(list_data) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split(',')

        def dfs():
            tmp = data.pop(0)
            # 读取并构造节点
            if tmp == 'null':
                return None
            node = TreeNode(int(tmp))
            node.left = dfs()
            node.right = dfs()
            # 返回构造好的当前节点
            return node

        root = dfs()
        return root


if __name__ == '__main__':
    try1 = Codec()
    null = None
    root1 = [1, 2, 3, null, null, 4, 5]
    root1 = ListToTree(root1)
    step1 = try1.serialize(root1)
    step2 = try1.deserialize(step1)
    print(TreeToList(step2))
