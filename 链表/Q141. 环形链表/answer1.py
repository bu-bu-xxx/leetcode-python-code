# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，双指针
# 内存O(1)
from 链表.ListNode.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        quick = head
        if not head:
            return False
        while quick.next is not None and quick.next.next is not None:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False







