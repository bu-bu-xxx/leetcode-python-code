# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LinkedList(list):
    """
    :param list: 输入列表
    :return: 输出单链表的头部
    """
    prev = ListNode()
    node = prev
    for i in list:
        node.next = ListNode(i)
        node = node.next
    return prev.next
