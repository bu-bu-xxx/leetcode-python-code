# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，迭代
# 是先序遍历，变回树，优先生成左子节点
# 用栈存已经存好值的节点
# 当有子节点，则生成新子节点，并入栈
# 当没有子节点，则出栈直到找到该插入新右子节点的地方
# 栈的长度=横杠数量+1
# 可以根据横杠数量直接出栈，栈顶即为该插入新右子节点的位置
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        import re
        change = re.findall(r'(\D*)(\d+)', traversal)
        stack = []
        for index, val in change:
            index = len(index)
            val = int(val)
            # 插入左节点
            if len(stack) == index:
                if not stack:
                    stack.append(TreeNode(val))
                else:
                    new_node = TreeNode(val)
                    stack[-1].left = new_node
                    stack.append(new_node)
            # 插入右节点
            else:
                stack = stack[:index]
                new_node = TreeNode(val)
                stack[-1].right = new_node
                stack.append(new_node)

        return stack[0]


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    traversal1 = "1-2--3--4-5--6--7"
    print(TreeToList(try1.recoverFromPreorder(traversal1)))
