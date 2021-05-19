# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 评论的更好的答案
# 拆成列表做
# 我稍加改进，改进后速度更慢
# 是因为用字典搜索比列表搜索快很多。虽然每次重新生成字典，但是还是快
from 链表.ListNode.ListNode import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a += [head.val]
            head = head.next

        def find(List, target):
            for i1, v1 in enumerate(List):
                if v1 == target:
                    return i1 + 1
            return False

        t = 0
        d = [0]
        ii = 0
        for v in a:
            t += v
            if temp := find(d, t):
                a = a[: temp - 1] + a[ii + 1:]
                d = d[:temp]
                t = d[-1]
                ii = temp - 2
            else:
                d.append(t)
            ii += 1

        ans = ListNode(0)
        t = ans
        for i in a:
            t.next = ListNode(i)
            t = t.next
        return ans.next


if __name__ == '__main__':
    from 链表.ListNode.ListNode import LinkedList, readLinkedList

    try1 = Solution()

    head1 = LinkedList([1, 3, 2, -3, -2, 5, 5, -5, 1])
    print(readLinkedList(try1.removeZeroSumSublists(head1)))

"""
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a += [head.val]
            head = head.next
        flag = True
        while flag:
            t = 0
            d = {0: -1}
            flag = False
            for i, v in enumerate(a) :
                t += v
                if t in d:
                    a = a[: d[t] + 1] + a[i + 1:]
                    flag = True
                    break
                d[t] = i
        ans = ListNode(0)
        t = ans
        for i in a:
            t.next = ListNode(i)
            t = t.next
        return ans.next

"""
