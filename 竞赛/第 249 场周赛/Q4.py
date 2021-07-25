# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5810. 合并多棵二叉搜索树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import List
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        roots_val = set(tree.val for tree in trees)
        n = len(trees)
        val_tree = {tree.val: tree for tree in trees}

        # find root
        leaf_set = set()
        for tree in trees:
            if tree.right:
                leaf_set.add(tree.right.val)
            if tree.left:
                leaf_set.add(tree.left.val)
        root = [tree for tree in trees if tree.val not in leaf_set]
        if len(root) != 1:
            return None

        # insert root, n-1 times
        leaf_queue = collections.deque()
        time = 1
        if root[0].left:
            leaf_queue.append(root[0].left)
        if root[0].right:
            leaf_queue.append(root[0].right)

        while time <= n - 1:
            if not leaf_queue:
                return None
            tmp = leaf_queue.popleft()
            if tmp.val in roots_val:
                roots_val -= {tmp.val}
                tmp.left = val_tree[tmp.val].left
                tmp.right = val_tree[tmp.val].right
                if tmp.left:
                    leaf_queue.append(tmp.left)
                if tmp.right:
                    leaf_queue.append(tmp.right)
                time += 1

        # check
        flag = True

        def check(node: TreeNode):
            nonlocal flag
            if node.left and (lt := check(node.left)) and lt[1] >= node.val:
                flag = False
                return
            if flag is False:
                return
            if node.right and (rt := check(node.right)) and rt[0] <= node.val:
                flag = False
                return
            if flag is False:
                return
            min_val, max_val = node.val, node.val
            if node.left:
                min_val = lt[0]
            if node.right:
                max_val = rt[1]
            return min_val, max_val

        check(root[0])
        if flag is False:
            return None
        return root[0]


if __name__ == "__main__":
    try1 = Solution()
    root1 = TreeNode(2, right=TreeNode(3))
    root2 = TreeNode(1, right=TreeNode(3))
    root3 = TreeNode(3, left=TreeNode(2))
    trees1 = [root1, root2, root3]
    print(try1.canMerge(trees1))
