# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 双端队列，单调队列，官方答案
# 队列从左到右单调递减，队列存放nums中的坐标
# 队列右边出去比新数小的所有坐标，然后加入新数坐标
# 队列左边出去坐标在窗口外的，然后读取最大数
# 这样可以保证队列单调递减，并且可证明可行性
# 可以理解成，队列中坐标表示这个位置前k个数的最大数，的坐标

class Solution:
    def maxSlidingWindow(self, nums, k):
        import collections
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans








