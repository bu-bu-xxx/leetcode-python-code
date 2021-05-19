# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，迭代
# 就是每k个迭代一次反转
from 链表.ListNode.ListNode import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 方便运算
        hair = ListNode()
        hair.next = head

        # 计算够不够k个数
        def bool_k(temp_hair1, temp_k):
            temp1 = temp_hair1
            for _ in range(temp_k):
                if not temp1.next:
                    return None, False
                temp1 = temp1.next
            return temp1.next, True

        # 开始的特殊情况
        if not head:
            return head
        # 迭代，反转
        temp_hair = hair
        while 1:
            (temp_last, temp_bool) = bool_k(temp_hair, k)
            if not temp_bool:
                return hair.next
            next_hair = temp_hair.next
            temp_slow = temp_hair.next
            temp_fast = temp_slow.next
            for _ in range(k - 1):
                temp = temp_fast.next
                temp_fast.next = temp_slow
                temp_slow = temp_fast
                temp_fast = temp
            next_hair.next = temp_last
            temp_hair.next = temp_slow

            # 切换到下一轮操作
            temp_hair = next_hair


if __name__ == '__main__':
    from 链表.ListNode.ListNode import LinkedList

    try1 = Solution()

    head = LinkedList([1, 2])
    k = 2
    print(try1.reverseKGroup(head, k))
