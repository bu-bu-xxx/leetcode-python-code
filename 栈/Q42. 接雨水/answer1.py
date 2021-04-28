# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 动态规划

# 从左到右扫描，实时更新目标方块左边最高的高度
# 同样从右到左，找出目标方块右边最高的高度
# min(左边最高和右边最高)-目标方块高度=储水量

class Solution:
    def trap(self, height) -> int:
        h_len = len(height)
        left_max = [0] * h_len
        right_max = [0] * h_len

        now_max = 0
        for i in range(h_len):
            now_max = max(now_max, height[i])
            left_max[i] = now_max

        now_max = 0
        for i in range(-1, -h_len - 1, -1):
            now_max = max(now_max, height[i])
            right_max[i] = now_max

        val = 0
        for i in range(h_len):
            now_val = min(left_max[i], right_max[i]) - height[i]
            val += now_val if now_val > 0 else 0

        return val


if __name__ == '__main__':
    try1 = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(try1.trap(height))
