# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ListToTree(List):
    """
    把null换成None
    :param List: 输入列表
    :return: 输出树的根部
    """
    root = TreeNode(val=List[0])
    temp = [root]
    for i in range(1, len(List)):
        if not List[i]:
            continue
        root_index = (i - 1) // 2
        new_node = TreeNode(val=List[i])
        if i % 2 == 1:
            temp[root_index].left = new_node
        else:
            temp[root_index].right = new_node
        temp.append(new_node)
    return root


def TreeToList(root):
    """
    None就是null
    :param root: 输入树的根节点
    :return: 返回列表
    """
    import collections
    temp = collections.deque()
    temp.append(root)
    result = [root.val]
    while temp:
        a = temp.popleft()
        if not a:
            continue
        al, ar = a.left,a.right
        if al:
            result.append(al.val)
        else:
            result.append(None)
        temp.append(al)
        if ar:
            result.append(ar.val)
        else:
            result.append(None)
        temp.append(ar)
    # 去除后面的None
    for i in result[-1::-1]:
        if i is None:
            result.pop()
        else:
            break
    return result


if __name__ == '__main__':
    list1 = [1, 2, None, 4]
    root1 = ListToTree(list1)
    print(TreeToList(root1))
