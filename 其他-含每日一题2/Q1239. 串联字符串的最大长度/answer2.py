# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，回溯+位运算
# 回溯有点像深度优先搜索
# 转变为二进制，数位上的1表示有这个数
# 总字符长度为count("1")
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 先存所有合法字符串的二进制值
        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                if (mask >> (ord(ch) - ord("a"))) & 1 == 0:
                    mask |= 1 << ord(ch) - ord("a")
                else:
                    mask = 0
                    break
            if mask != 0:
                masks.append(mask)

        # 回溯，inx未搜索，val上一个值
        res = 0

        def dfs(inx: int, val: int):
            if inx == len(masks):
                nonlocal res
                res = max(res, bin(val).count("1"))
                return
            if masks[inx] & val == 0:
                dfs(inx + 1, masks[inx] | val)
            dfs(inx + 1, val)

        dfs(0, 0)
        return res


if __name__ == "__main__":
    try1 = Solution()
    arr1 = ["cha", "r", "act", "ers"]
    print(try1.maxLength(arr1))
