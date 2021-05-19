# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方方法，穿针引线
# 只遍历一次，穿完全部
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        hair = ListNode()
        hair.next = head

        # 找到各种节点
        pre_point = hair
        for _ in range(left - 1):
            pre_point = pre_point.next
        left_point = pre_point.next
        right_point = left_point
        # 开始遍历，穿针引线
        now_point = left_point.next
        for _ in range(right - left):
            next_point = now_point.next
            now_point.next = left_point
            left_point = now_point
            now_point = next_point
        # 修饰开头结尾
        pre_point.next = left_point
        right_point.next = now_point

        return hair.next
