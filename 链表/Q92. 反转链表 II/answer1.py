# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 找到left，right对应的节点，然后反转
# 改了好多次，代码可读性不强
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 找到左右节点
        hair = ListNode()
        hair.next = head
        hair_point, right_point = hair, head
        for _ in range(left - 1):
            hair_point = hair_point.next
        for _ in range(right - 1):
            right_point = right_point.next

        # 反转
        left_point = hair_point.next
        temp1 = left_point
        temp2 = left_point.next
        last_point = right_point.next
        while temp1 != right_point:
            temp = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp
        left_point.next = last_point
        hair_point.next = right_point

        return hair.next


if __name__ == '__main__':
    from 链表.ListNode.ListNode import LinkedList, readLinkedList

    try1 = Solution()

    head = LinkedList([3, 5])
    print(readLinkedList(try1.reverseBetween(head, 1, 2)))
