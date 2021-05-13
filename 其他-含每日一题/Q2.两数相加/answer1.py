# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    l0 = ListNode()
    temp = l0
    jin = 0
    val = 0
    while l1 or l2 or jin:
        if l1:
            val = val + l1.val
            l1 = l1.next
        if l2:
            val = val + l2.val
            l2 = l2.next
        if jin:
            val = val + 1
        jin = val // 10
        val = val % 10
        temp.next = ListNode(val=val)
        temp = temp.next
        val = 0
    return l0.next


if __name__ == '__main__':
    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(val=3)

    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(val=4)

    l0 = addTwoNumbers(l1, l2)
    temp = l0
    while temp:
        print(temp.val)
        temp = temp.next
