# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 双指针
# 一层一层往上加水，一次加一格

class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0

        h_len = len(height)
        left_max = 0
        right_max = 0
        left_ad = 0
        right_ad = h_len - 1
        val = 0
        while left_ad != right_ad:
            if left_max < right_max:
                val += left_max - height[left_ad] if left_max > height[left_ad] else 0
                left_max = max(left_max, height[left_ad])
                left_ad += 1
            else:
                val += right_max - height[right_ad] if right_max > height[right_ad] else 0
                right_max = max(right_max, height[right_ad])
                right_ad -= 1
        # 最后相遇这一层
        last_max = min(left_max, right_max)
        val += last_max - height[left_ad] if last_max > height[left_ad] else 0

        return val


if __name__ == '__main__':
    try1 = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(try1.trap(height))
