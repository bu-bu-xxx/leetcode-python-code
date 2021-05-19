# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，迭代
# 两个两个交换
from 链表.ListNode.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Head是加上去的方便运算的头
        Head = ListNode()
        Head.next = head
        temp0 = Head
        # 迭代交换，temp0是前一个节点，要换temp1和temp2
        while (temp1 := temp0.next) is not None and (temp2 := temp1.next) is not None:
            temp1.next = temp2.next
            temp2.next = temp1
            temp0.next = temp2
            temp0 = temp1
        # 返回结果
        return Head.next






