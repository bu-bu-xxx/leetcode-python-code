# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自答，遍历每一个，得到n个最大面积

class Solution:
    def find(self, heights, tag):
        left = tag
        right = tag
        h = heights[tag]
        for i in range(tag, -1, -1):
            if heights[left] >= h and left != -1:
                left -= 1
            else:
                break
        for i in range(tag, len(heights), 1):
            if heights[right] >= h and right != len(heights):
                right += 1
            else:
                break
        return h * (right - left - 1)

    def largestRectangleArea(self, heights) -> int:
        a = []
        for tag in range(len(heights)):
            a.append(self.find(heights, tag))
        return max(a)


if __name__ == '__main__':
    try1 = Solution()

    heights = [1]*11
    print(try1.largestRectangleArea(heights))
