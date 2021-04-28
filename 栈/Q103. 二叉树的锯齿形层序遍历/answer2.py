# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 广度优先，分层搜索

# import collections
# collections.deque双端列表，头部插入与删除的时间复杂度为O(1)
# popleft,appendleft
# list(deque)还原变成list

# 1获取queue长度
# 2选择迭代次数
# 3出队列的值记录，分正序反序

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        import collections as col
        queue = col.deque([root])
        res = []
        row = 0  # 第几层
        while queue:
            queue_len = len(queue)
            res.append(col.deque())
            for time in range(queue_len):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                if row % 2 == 0:  # 奇数层
                    res[row].append(temp.val)
                else:  # 偶数层
                    res[row].appendleft(temp.val)
            row += 1

        return [list(i) for i in res]
