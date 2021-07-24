# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，回溯(这个我觉得没用到)+哈希表


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

        map_dict = dict()
        tmp = head
        new_head = Node(0)
        map_dict[head] = new_head
        map_dict[None] = None

        while tmp is not None:
            map_dict[tmp].val = tmp.val
            if tmp.next and tmp.next not in map_dict:
                map_dict[tmp.next] = Node(0)
            if tmp.random and tmp.random not in map_dict:
                map_dict[tmp.random] = Node(0)
            map_dict[tmp].next = map_dict[tmp.next]
            map_dict[tmp].random = map_dict[tmp.random]
            tmp = tmp.next

        return new_head


if __name__ == "__main__":
    try1 = Solution()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, a.random = b, None
    b.next, b.random = c, a
    c.next, c.random = None, None
    print(try1.copyRandomList(a).next.val)
