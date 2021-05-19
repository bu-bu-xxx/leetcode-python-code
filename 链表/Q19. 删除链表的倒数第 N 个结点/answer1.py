# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，暴力法
# 先计算总长度，再删除第n个
from 链表.ListNode.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        all_len = 0
        temp = head
        while temp is not None:
            all_len += 1
            temp = temp.next
        temp = head
        if all_len == n:
            return head.next
        for i in range(all_len - n - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
