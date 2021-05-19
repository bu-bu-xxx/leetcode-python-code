# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，哈希表
# 存在集合里面
from 链表.ListNode.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_set = set()
        while head is not None:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        return False


"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_set = set()
        while head is not None:
            if hash(head) in hash_set:
                return True
            hash_set.add(hash(head))
            head = head.next
        return False
"""
