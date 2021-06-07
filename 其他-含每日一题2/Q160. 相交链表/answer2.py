# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，巧妙的方法
# 空间复杂度O(1)
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode-solutio-a8jn/
# 方法：双指针
from 链表.ListNode.ListNode import ListNode, LinkedList


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA = headA
        tmpB = headB
        while tmpA is not None or tmpB is not None:
            if tmpB == tmpA:
                return tmpA
            if tmpB is None:
                tmpB = headA
                continue
            elif tmpA is None:
                tmpA = headB
                continue
            tmpB = tmpB.next
            tmpA = tmpA.next
        return None






