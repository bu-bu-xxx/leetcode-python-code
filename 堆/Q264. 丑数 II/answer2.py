# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 堆，答案
# 复杂度O(n*log(n))
# 第n次出堆即为所求
# 每次出堆都入堆2*ans，3*ans，5*ans
# 用集合存不重复的丑数

class Solution:
    def nthUglyNumber(self, n):
        import heapq
        heap = [1]
        diff = {1}
        nums = [2, 3, 5]
        for i in range(n):
            temp = heapq.heappop(heap)
            for num in nums:
                if (ans := num * temp) not in diff:
                    diff.add(ans)
                    heapq.heappush(heap, ans)
        return temp
