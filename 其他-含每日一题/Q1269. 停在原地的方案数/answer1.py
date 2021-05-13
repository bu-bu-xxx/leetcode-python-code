# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，队列
# 先进step=0的位置
# 每次弹出队列所有位置，再入队列下一步可能到的位置
# 所有step操作完之后，找出队列中在0的位置
# 存(position,num)到队列中，先用dict累加好再存

class Solution:
    def numWays(self, steps, arrLen):
        import collections
        queue = collections.deque([(0, 1)])
        for _ in range(steps):
            # 一次遍历当前steps的所有点，存入字典
            temp_dict = collections.Counter()
            for i in range(len(queue)):
                (position, num) = queue.popleft()
                temp_dict[position - 1] += num
                temp_dict[position] += num
                temp_dict[position + 1] += num
            # 从字典读取，存入queue
            for position, num in temp_dict.items():
                if 0 <= position < arrLen:
                    queue.append((position, num))
        # 最后读取在0点的数量
        for j in queue:
            if j[0] == 0:
                return j[1] % (10 ** 9 + 7)


if __name__ == '__main__':
    try1 = Solution()

    steps = 3
    arrLen = 2
    print(try1.numWays(steps, arrLen))
