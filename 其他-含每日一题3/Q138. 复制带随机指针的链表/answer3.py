# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，
# 我们首先将该链表中每一个节点拆分为两个相连的节点，例如对于链表A->B->C，我们可以将其拆分为
# A->A'->B->B'->C->C'。对于任意一个原节点S，其拷贝节 S'即为其后继节点。
# 这样，我们可以直接找到每一个拷贝节点 S'的随机指针应当指向的节点，
# 即为其原节点S的随机指针指向的节点T的后继节点T'。


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        tmp = head
        while tmp:
            new_node = Node(tmp.val)
            new_node.next = tmp.next
            tmp.next = new_node
            tmp = new_node.next

        tmp = head
        while tmp:
            tmp.next.random = tmp.random.next if tmp.random else None
            tmp = tmp.next.next

        tmp = head
        while tmp and tmp.next.next:
            tmp_next = tmp.next.next
            tmp.next.next = tmp.next.next.next
            tmp = tmp_next

        return head.next


if __name__ == "__main__":
    try1 = Solution()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, a.random = b, None
    b.next, b.random = c, a
    c.next, c.random = None, None
    print(try1.copyRandomList(a).val)
