# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，解释规则法
# 简单
from 链表.ListNode.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        now = ListNode()
        result = now
        temp = 0
        while l1 is not None or l2 is not None or temp != 0:
            (a, l1) = (0, l1) if not l1 else (l1.val, l1.next)
            (b, l2) = (0, l2) if not l2 else (l2.val, l2.next)
            now.next = ListNode((a + b + temp) % 10)
            temp = (a + b + temp) // 10  # 进位
            now = now.next
        return result.next
