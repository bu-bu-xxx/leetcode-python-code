# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 留一个数组，记录第i个位置连续加到当前点的各数值
# 找到等于0的删除这一段
# 然后更新数组，继续
from 链表.ListNode.ListNode import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        record = []
        hair = ListNode()
        hair.next = head
        now_node = head
        pre_node = hair
        # 遍历链表
        while now_node:
            # 节点值为0
            if (add_val := now_node.val) == 0:
                pre_node.next = now_node.next
                # 检查下一个节点
                now_node = now_node.next

            # 不为0时
            else:
                # 更新record数组值后找是否有等于0的
                record.append(0)
                record = [i + add_val for i in record]
                for i, val in enumerate(record):
                    # 如果找到等于0的，就更新record，并修改链表
                    if val == 0:
                        record = record[0:i]
                        record = [j - val for j in record]
                        # 修改链表
                        pre = hair
                        for _ in range(i):
                            pre = pre.next
                        pre.next = now_node.next
                        pre_node = pre
                        break
                # 检查下一个节点
                else:
                    pre_node = pre_node.next
                now_node = now_node.next

        return hair.next
