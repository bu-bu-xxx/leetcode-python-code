# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 单调栈，大的入栈，小的出栈直到看到小的
# 编号代表最左可以到哪一格子
# 左单调栈处理一次，反过来右单调栈处理一次

def zhan(heights):
    h_len = len(heights)

    stack = []
    record = []
    for i in range(h_len):
        while stack and heights[i] <= heights[stack[-1]]:
            stack.pop()
        record.append(stack[-1] if stack else -1)
        stack.append(i)

    return record


class Solution:

    def largestRectangleArea(self, heights) -> int:
        left = zhan(heights)
        re_heights = heights[-1:-len(heights) - 1:-1]
        right = zhan(re_heights)
        a = []
        for i in range(len(right) - 1, -1, -1):
            a.append(len(heights) - 1 - right[i])
        right = a

        val = []
        for i in range(len(left)):
            val.append((right[i] - left[i] - 1) * heights[i])

        return max(val)


if __name__ == '__main__':
    try1 = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    print(try1.largestRectangleArea(heights))
