# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先遍历
# data是列表的str
# 备注：这题oj有问题，它不检查序列化之后的东西，
# 只检查序列化再反序列化，能不能回到原来的样子
from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        import collections
        queue = collections.deque([root])
        res = []  # 存str
        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp is None:
                    res.append('null')
                else:
                    res.append(str(tmp.val))
                    queue.append(tmp.left)
                    queue.append(tmp.right)
        # 输出，删除末尾null
        for tail in res[-1::-1]:
            if tail == 'null':
                res.pop()
            else:
                break
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None

        import re, collections
        # data = re.findall(r'([-0-9a-z]+)', data)
        data = data[1:-1].split(',')  # 这个更好
        len_data = len(data)
        index = 1
        queue = collections.deque([TreeNode(int(data[0]))])
        root = queue[0]
        # 一次出队列，搜索两个子节点
        while queue:
            tmp = queue.popleft()
            # 左节点，空节点不进队列
            if index >= len_data:
                break
            if data[index] != 'null':
                tmp.left = TreeNode(int(data[index]))
                queue.append(tmp.left)
            index += 1
            # 右节点
            if index >= len_data:
                break
            if data[index] != 'null':
                tmp.right = TreeNode(int(data[index]))
                queue.append(tmp.right)
            index += 1

        return root


if __name__ == '__main__':
    try1 = Codec()
    null = None
    root1 = [1, 2, 3, null, null, 4, 5]
    root1 = ListToTree(root1)
    print(try1.serialize(root1))
    print(TreeToList(try1.deserialize(try1.serialize(root1))))
