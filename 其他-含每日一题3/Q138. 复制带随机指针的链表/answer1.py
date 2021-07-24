# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，编号，哈希表
# 废空间


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

        hand_num = dict()
        tmp = head
        num = 0
        while tmp:
            hand_num[tmp] = num
            num += 1
            tmp = tmp.next

        num_hand = [Node(0) for _ in range(num)]
        tmp = head
        num = 0
        while tmp:
            num_hand[num].val = tmp.val
            if tmp.next:
                num_hand[num].next = num_hand[hand_num[tmp.next]]
            if tmp.random:
                num_hand[num].random = num_hand[hand_num[tmp.random]]
            tmp = tmp.next
            num += 1

        return num_hand[0]


if __name__ == "__main__":
    try1 = Solution()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, a.random = b, None
    b.next, b.random = c, a
    c.next, c.random = None, None
    print(try1.copyRandomList(a).val)
