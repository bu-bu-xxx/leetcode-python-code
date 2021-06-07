# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，哈希表
# 简单，但是内存复杂度是 O(n)，太高，超出时间限制
from 链表.ListNode.ListNode import ListNode, LinkedList


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 构建哈希表
        hash_list = []
        while headA is not None:
            hash_list.append(headA)
            headA = headA.next
        # 搜索B
        while headB is not None:
            if headB in hash_list:
                return headB
            headB = headB.next
        return None
