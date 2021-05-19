# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，迭代
# 简单
from 链表.ListNode.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        new_head = ListNode()
        temp = new_head
        while 1:
            if l1 is None or l2 is None:
                temp.next = l1 if not l2 else l2
                return new_head.next
            (temp.next, l1, l2) = (l1, l1.next, l2) if l1.val <= l2.val \
                else (l2, l1, l2.next)
            temp = temp.next
