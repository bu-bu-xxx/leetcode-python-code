# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 队列解决，先进先出
# 先按层得到遍历，再变成锯齿状

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result1 = []
        queue = [root]
        ceng_list = []
        ceng_queue = [1]
        while queue:
            temp = queue.pop(0)
            ceng_temp = ceng_queue.pop(0)
            ceng_list.append(ceng_temp)
            if temp.left:
                queue.append(temp.left)
                ceng_queue.append(ceng_temp + 1)
            if temp.right:
                queue.append(temp.right)
                ceng_queue.append(ceng_temp + 1)
            result1.append(temp.val)

        # 分层
        i = 0
        ceng_all = max(ceng_list)
        result2 = [0] * ceng_all
        for ceng in range(1, ceng_all + 1):
            temp = []
            while i < len(ceng_list) and ceng_list[i] == ceng:
                temp.append(result1[i])
                i += 1

            result2[ceng - 1] = temp

        # 锯齿状
        result3 = [0] * ceng_all
        i = 0
        for t in range(len(result2)):
            temp = result2[t]
            ans = temp.copy()
            if t % 2 == 1:
                for a in range(len(temp)):
                    ans[-a - 1] = temp[a]
                result3[i] = ans
            else:
                result3[i] = ans
            i += 1

        return result3
