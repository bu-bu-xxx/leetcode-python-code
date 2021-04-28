# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用heapq包做

class Solution:
    def lastStoneWeight(self, stones) -> int:
        import heapq
        # 变成相反数
        stones = [-i for i in stones]
        # temp_stones = stones.copy()
        # for i in range(len(stones)):
        #     temp_stones[i] = stones[i]*(-1)
        # stones = temp_stones

        heapq.heapify(stones)
        while len(stones) > 1:
            temp1 = heapq.heappop(stones)
            temp2 = heapq.heappop(stones)
            if temp1 == temp2:
                continue
            else:
                new = -abs(temp1 - temp2)
                heapq.heappush(stones, new)
        if len(stones) == 0:
            return 0
        return -stones[0]


if __name__ == '__main__':
    try1 = Solution()

    stones = [2, 7, 4, 1, 8, 1]
    print(try1.lastStoneWeight(stones))
