# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LinkedList(List):
    """
    :param List: 输入列表
    :return: 输出单链表的头部
    """
    prev = ListNode()
    node = prev
    for i in List:
        node.next = ListNode(i)
        node = node.next
    return prev.next


def readLinkedList(head):
    """
    :param head: 头指针
    :return: 链表值的数组
    """
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result
