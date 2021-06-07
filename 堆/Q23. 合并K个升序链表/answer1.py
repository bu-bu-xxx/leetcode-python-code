# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 暴力法
# 全部数取出来，然后排序，再合成链表
# 时间复杂度是O(n*log(n))，空间复杂度是O(n)
from 链表.ListNode.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists):
        prev = ListNode()  # 头部的前面一个点
        all_list = []
        if not lists:
            return prev.next

        for list in lists:
            while list:
                all_list.append(list.val)
                list = list.next
        if not all_list:
            return prev.next
        temp = prev
        all_list = sorted(all_list)
        for i in all_list:
            temp.next = ListNode(i)
            temp = temp.next
        return prev.next


if __name__ == '__main__':
    try1 = Solution()
