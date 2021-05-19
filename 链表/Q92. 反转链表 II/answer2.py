# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，选取中间那段反转
# left前面是pre，right后面是post
# 注意切断pre和left连接，right和post连接
# 反转好后接回去
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 简化运算
        hair = ListNode()
        hair.next = head

        # 反转中间那段
        def reverse(begin, end):
            if begin == end:
                return
            temp1 = begin
            temp2 = begin.next
            while temp1 != end:
                temp = temp2.next
                temp2.next = temp1
                temp1, temp2 = temp2, temp

        # 找到pre和post
        pre, right_point = hair, hair
        for _ in range(left - 1):
            pre = pre.next
        for _ in range(right):
            right_point = right_point.next
        left_point = pre.next
        post = right_point.next
        # 删除前后联系
        pre.next = None
        right_point.next = None

        # 正式反转中间那段
        reverse(left_point, right_point)
        pre.next = right_point
        left_point.next = post
        return hair.next
