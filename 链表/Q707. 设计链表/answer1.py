# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._hair = ListNode()
        self.all_len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index > (self.all_len - 1):
            return -1
        temp = self._hair
        for _ in range(index + 1):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the
        linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        new = ListNode(val, self._hair.next)
        self._hair.next = new
        self.all_len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the
        linked list.
        """
        last_point = self._hair
        while last_point.next:
            last_point = last_point.next
        last_point.next = ListNode(val)
        self.all_len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in
        the linked list. If index equals to the length of
        linked list, the node will be appended to the end of
        linked list. If index is greater than the length,
        the node will not be inserted.
        """
        if index < 0:
            self.addAtHead(val)
        elif index > self.all_len:
            return
        else:
            pre = self._hair
            for _ in range(index):
                pre = pre.next
            post = pre.next
            new = ListNode(val, post)
            pre.next = new
            self.all_len += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the
        index is valid.
        """
        if 0 <= index < self.all_len:
            pre = self._hair
            for _ in range(index):
                pre = pre.next
            post = pre.next.next
            pre.next = post
            self.all_len -= 1
