# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，Morris算法
# 算法过程和代码：https://blog.csdn.net/yangfeisc/article/details/45673947
# 可以实现空间复杂度O(1)，同时时间复杂度由栈的O(N)增加成O(2N)
# Morris算法的中序遍历：
# 1.如果当前节点cur没有左节点，则输出cur.val，cur=cur右节点
# 2.如果cur有左节点，找到cur的左节点的最右节点，即为cur的前驱节点pre
# 2.1.如果是第一次遍历到pre，则pre的右节点连接到cur，cur=cur左节点
# 2.2.如果第二次遍历到pre(pre右节点是cur)，则切断pre右节点是cur，
# 并输出cur.val，取cur=cur右节点
# 3.直到cur为空节点为止
# 找错误点：
# 1.存降序排列的相邻两个数
# 2.遍历完分找到一组和两组错误点，把值调整
from 树.TreeNode.TreeNode import TreeNode,TreeToList,ListToTree


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        wrong_node = []
        wrong_pre = [TreeNode(float('-inf'))] # 临时前驱点

        # 判断是否为错误点
        def judge(node):
            if wrong_pre[0].val>= node.val:
                wrong_node.append([wrong_pre[0],node])
            wrong_pre[0] = node

        # Morris
        cur = root
        while cur is not None:
            # 没有左节点
            if cur.left is None:
                judge(cur)
                cur = cur.right
            # 有左节点
            else:
                # 找到cur的前驱节点
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                # 第一次遍历到
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                # 第二次
                else:
                    pre.right = None
                    judge(cur)
                    cur = cur.right

        # 调整错误点
        if len(wrong_node) == 1:
            wrong_node[0][0].val,wrong_node[0][1].val = \
                wrong_node[0][1].val,wrong_node[0][0].val
        else:
            wrong_node[0][0].val, wrong_node[1][1].val = \
                wrong_node[1][1].val, wrong_node[0][0].val


if __name__ == '__main__':
    try1 = Solution()
    null = None
    root1 = [3, 1, 4, null, null, 2]
    root1 = ListToTree(root1)
    try1.recoverTree(root1)
    print(TreeToList(root1))

