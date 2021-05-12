# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 快速排序方法，是一种分治算法
# 适用于确定数据量的数组，动态数据量用堆
# 可以证明时间复杂度是O(n)

# 注：用快速排序把数组从小到大排列好，时间复杂度O(n*ln(n))，不是本题
# 证明一种是归纳法，一种是递归，用到1/n求和的近似值估计

# 算法思想：快速排序(用双指针)，和分治算法思想
# 具体：
# 1.对low，high中间随机选一个pivot作为基准值base
# 2.慢指针对应左边都是比base大的数，快指针遍历low到high
# 3.完成一次快速排序
# 4.分治部分：如果pivot位置恰好为k则return，否则在pivot左边或右边继续快速排序，用递归

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import random
        def findK(low, high):
            # 加入随机选pivot，提高leetcode上面的效率
            temp = random.randint(low, high)
            nums[low], nums[temp] = nums[temp], nums[low]
            pivot = low
            # 慢指针low+1开始，快指针也是，慢指针左边都是大的数
            i, j = low + 1, low + 1
            base = nums[pivot]
            for j in range(low + 1, high + 1):
                if nums[j] > base:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[pivot], nums[i - 1] = nums[i - 1], nums[pivot]
            i -= 1
            if i == k - 1:
                return nums[i]
            if i < k - 1:
                return findK(i + 1, high)
            if i > k - 1:
                return findK(low, i - 1)

        return findK(0, len(nums) - 1)


if __name__ == '__main__':
    try1 = Solution()

    nums, k = [3, 2, 1, 5, 6, 4], 2
    print(try1.findKthLargest(nums, k))
