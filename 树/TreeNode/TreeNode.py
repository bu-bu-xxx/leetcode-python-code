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
    # 构造一个队列
    # 队列存节点，同时指针遍历List
    # 同广度遍历一样
    import collections
    queue = collections.deque()
    root = TreeNode(List[0])
    queue.append(root)
    index = 0
    while index < len(List) - 1:
        temp = queue.popleft()
        # 如果是空节点
        if temp is None:
            continue
        # 左节点
        index += 1
        if List[index] is not None:
            temp.left = TreeNode(List[index])
            queue.append(temp.left)
        else:
            queue.append(temp.left)
        # 右节点
        index += 1
        if index < len(List) and List[index] is not None:
            temp.right = TreeNode(List[index])
            queue.append(temp.right)
        else:
            queue.append(temp.right)

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
        al, ar = a.left, a.right
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
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = ListToTree(list1)
    print(TreeToList(root1))
