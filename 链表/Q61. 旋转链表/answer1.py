# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，闭合成环
# 先遍历一遍，找到尾巴
# 再切断倒数第k个
from 链表.ListNode.ListNode import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 特殊情况
        if not head:
            return head
        # 计算总长度
        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next
        # 补成环
        temp.next = head

        # 切断
        k = k % count
        cut = head
        for _ in range(count - k - 1):
            cut = cut.next
        new_head = cut.next
        cut.next = None

        return new_head
