# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 单向栈

# 递减的栈，每次出栈水填平，以栈顶及当前的高度为左右容器高度
# 横向放水， 栈空为0高度

class Solution:
    def trap(self, height) -> int:
        stack = []
        h_len = len(height)
        val = 0
        for i in range(h_len):
            while stack and height[stack[-1]] <= height[i]:
                now_h = height[stack.pop()]
                left_ad = stack[-1] if stack else -1
                right_h = height[i]
                right_ad = i
                left_h = height[left_ad] if left_ad != -1 else 0
                h = min(left_h, right_h) - now_h
                h = 0 if h <= 0 else h
                val += (right_ad - left_ad - 1) * h
            stack.append(i)

        return val


if __name__ == '__main__':
    try1 = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(try1.trap(height))
