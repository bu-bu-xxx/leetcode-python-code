# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 分治法，官方答案以及高分答案
# k个链表合成k/2个，再k/4，以此直到合成一个
# k = len(lists)
# 时间复杂度O(k*n*log(k))，空间复杂度O(log(k))
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

        lists_copy = lists.copy()
        while len(lists_copy) != 1:
            for k in range(0, len(lists_copy) // 2):
                temp = merge2(lists_copy[k], lists_copy[k + 1])
                del lists_copy[k]
                lists_copy[k] = temp
        return lists_copy[0]


if __name__ == '__main__':
    from 链表.ListNode.ListNode import LinkedList

    try1 = Solution()

    lists = [LinkedList([1, 4, 5]), LinkedList([1, 3, 4]), LinkedList([2, 6])]
    print(try1.mergeKLists(lists).val)
