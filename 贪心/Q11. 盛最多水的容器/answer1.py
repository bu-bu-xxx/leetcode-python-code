# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，双指针
# 证明：
# 1.假设最左端以x为界，最右端以y为界
# 不妨设x<=y，则以x为左界，右界往左移动，不可能找到装更多水的容器了
# 所以只能移动左界
# 2.固定x0左界，y0右界，只能在左界右界之间找x1和y1
# 因为如果有x1在[x0,y0]之外，则一定会经过1步骤
# 断定边界为[x1,y0]时，以x1为边界的任何yk<=y都不行，(此时y>=y0)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        res = (high - low) * min(height[high], height[low])
        while low != high:
            if height[low] <= height[high]:
                low += 1
                res = max(res, (high - low) * min(height[low], height[high]))
            else:
                high -= 1
                res = max(res, (high - low) * min(height[low], height[high]))
        return res
