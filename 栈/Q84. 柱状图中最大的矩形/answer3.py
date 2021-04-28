# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 单调栈 + 常数优化
# 只用一次单调栈

class Solution:
    def largestRectangleArea(self, heights) -> int:
        h_len = len(heights)
        stack = []
        record = []
        val = []
        for i in range(h_len):
            while stack and heights[i] <= heights[stack[-1]]:
                a = stack.pop()
                val.append((i - record[a] - 1) * heights[a])
            record.append(stack[-1] if stack else -1)
            stack.append(i)
        while stack:
            a = stack.pop()
            val.append((len(heights) - record[a] - 1) * heights[a])
        return max(val)


if __name__ == '__main__':
    try1 = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    print(try1.largestRectangleArea(heights))
