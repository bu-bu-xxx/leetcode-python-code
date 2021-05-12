# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 暴力法
# 一次合并两个成一个，用两个指针，一共合并k-1次
# k = len(lists)
# 时间复杂度O(k2*n)，空间复杂度O(1)
from 链表.ListNode.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        def merge2(A, B):
            prev = ListNode()
            temp = prev
            A_temp, B_temp = A, B
            while 1:
                if not A_temp:
                    temp.next = B_temp
                    temp = temp.next
                    break
                if not B_temp:
                    temp.next = A_temp
                    temp = temp.next
                    break
                if A_temp.val > B_temp.val:
                    temp.next = B_temp
                    B_temp = B_temp.next
                    temp = temp.next
                else:
                    temp.next = A_temp
                    A_temp = A_temp.next
                    temp = temp.next
            return prev.next

        lists.append(None)
        begin = lists[0]
        for other_node in range(1, len(lists)):
            begin = merge2(begin, lists[other_node])
        return begin


if __name__ == '__main__':
    from 链表.ListNode.ListNode import LinkedList
    try1 = Solution()

    lists = [LinkedList([1, 4, 5]), LinkedList([1, 3, 4]), LinkedList([2, 6])]
    print(try1.mergeKLists(lists).val)
