# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，递归
# 每次递归return这个节点下的树，的最大值和最小值
# 递归，和左右子树最大值比较，和左右子树最小值比较
# 发现节点值<=左子树最大值，或者>=右子树最小值，存(当前节点，左子树最大值，右子树最小值)
# 最后再从该节点左子树找最大值(右子树最小值)，交换两个节点或者三个节点值即可

# 这个算法复杂度太高，主要是一开始没设计好，后面修改花了很多时间，效果也不好
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        record = [None, None, None]  # 存错误的节点，和下一个错误点在左子树或右子树，和最值

        def dfs(node):
            # 递归函数return当前节点的树的(最大值，最小值)
            left_val = dfs(node.left) if node.left else (float('-inf'), float('inf'))
            right_val = dfs(node.right) if node.right else (float('-inf'), float('inf'))
            # 找错误点，(node,left,right)
            node_val = node.val
            if node_val <= left_val[0] or node_val >= right_val[1]:
                record[:] = [node, left_val[0], right_val[1]]
            # 返回最大值最小值
            return max(left_val[0], right_val[0], node_val), \
                   min(left_val[1], right_val[1], node_val)

        dfs(root)
        # 通过错误节点找到第二个错误节点
        import collections
        record_sec = collections.deque([record[0]])
        begin_all = []
        if record[1] not in [float('inf'), float('-inf')]:
            begin_all.append((record[0].left, 'left', record[1]))
        if record[2] not in [float('inf'), float('-inf')]:
            begin_all.append((record[0].right, 'right', record[2]))
        # 广度优先搜索，找到三个点
        for i in begin_all:
            begin = i[0]
            queue = collections.deque()
            queue.append(begin)
            while queue:
                temp = queue.popleft()
                if not temp:
                    continue
                if temp.val == i[2]:
                    # 选择插入record_sec的位置
                    if i[1] == 'left':
                        record_sec.appendleft(temp)
                    else:
                        record_sec.append(temp)
                    break
                queue.append(temp.left)
                queue.append(temp.right)
        # 修改值
        record_new = sorted(record_sec, key=lambda x: x.val)
        record_sec = [x.val for x in record_sec]
        for i, x in enumerate(record_new):
            x.val = record_sec[i]


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    null = None
    root1 = [1, 3, null, null, 2]
    root1 = ListToTree(root1)
    try1.recoverTree(root1)
    print(TreeToList(root1))
