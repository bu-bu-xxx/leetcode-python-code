# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归
# 先递归下面的指针
# 然后nk.next.next = nk
# 递归的意思是nk后面的(不包括nk)next指针都改完
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseList(self, head):
        if head is None:
            return head

        def change_nk(nk):
            if (nk_next := nk.next) is None:
                return nk
            new_head = change_nk(nk_next)
            nk_next.next = nk
            return new_head

        new_head = change_nk(head)
        head.next = None
        return new_head
