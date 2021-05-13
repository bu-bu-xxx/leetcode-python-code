# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，最大堆
# 每次进一个(val,index)，看堆顶时的时候如果index不在窗口内，则出堆
# 最坏情况时间复杂度O(n*log(n))

class Solution:
    def maxSlidingWindow(self, nums, k):
        import heapq
        # 构建堆
        heap = [(-val, index) for (index, val) in enumerate(nums[0:k])]
        heapq.heapify(heap)
        result = []
        nums.append(123)
        # 进堆，及查看堆顶，及出堆
        for i in range(k, len(nums)):
            while (temp := heap[0])[1] < i - k:
                heapq.heappop(heap)
            result.append(-heap[0][0])
            heapq.heappush(heap, (-nums[i], i))
        return result
