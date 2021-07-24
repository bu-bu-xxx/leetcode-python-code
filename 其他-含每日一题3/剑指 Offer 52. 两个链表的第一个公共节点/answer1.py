# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学
# ez


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from 链表.ListNode.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        nodeA = headA
        nodeB = headB
        while 1:
            if nodeA == nodeB:
                return nodeB
            nodeA = nodeA.next
            nodeB = nodeB.next
            if nodeB is None and nodeA is None:
                break
            if nodeA is None:
                nodeA = headB
            if nodeB is None:
                nodeB = headA

        return None
