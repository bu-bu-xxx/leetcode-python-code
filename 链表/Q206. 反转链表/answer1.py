# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 迭代
# 只改指针，不读数据
# 把前面指向后面的指针，转成后面指向前面
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        first, second = head, head.next
        while second is not None:
            temp_sec = second.next
            second.next = first
            first = second
            second = temp_sec
        head.next = None
        return first
