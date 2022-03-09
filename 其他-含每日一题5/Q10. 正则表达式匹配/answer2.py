# encoding:utf-8
# @Author :ZQY


# 参考官方答案，还是有难度，动态规划
# 状态转移方程：
# i表示s的索引，j表示分好的p_re索引，默认是False
# dp[i][j] = p[i][j-1]  if p_re[j]有*
#                       p[i-1][j] or p[i-1][j-1]  if p_re[j]==. or s[i]
#            p[i-1][j-1]  if p_re[j]没有* and p_re[j]==. or s[i]
# 备注：可以和官方答案一样，不区分'a'和'a*'，是可以实现更简洁的状态转移方程的，
# 可以改但是没必要。
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_re = re.findall(r'[^\*][\*]*', p)

        # 初始化
        dp = [False] * len(p_re)
        rec = 0
        for j in range(len(p_re)):
            if rec == 1 and len(p_re[j]) == 1:
                break
            if len(p_re[j]) == 1 and p_re[j] not in ['.', s[0]]:
                break
            elif len(p_re[j]) == 1 and p_re[j] in ['.', s[0]]:
                dp[j] = True
                rec += 1
            elif len(p_re[j]) == 2 and p_re[j][0] not in ['.', s[0]]:
                dp[j] = dp[j - 1] if j - 1 >= 0 else False
            elif len(p_re[j]) == 2 and p_re[j][0] in ['.', s[0]]:
                dp[j] = True

        # 迭代
        for i in range(1, len(s)):
            dp_nex = [False] * len(p_re)
            for j in range(len(p_re)):
                if len(p_re[j]) == 1 and p_re[j] in ['.', s[i]]:
                    dp_nex[j] = dp[j - 1] if j - 1 >= 0 else dp_nex[j]
                elif len(p_re[j]) == 2:
                    dp_nex[j] = dp_nex[j] | dp_nex[j - 1] if j - 1 >= 0 else dp_nex[j]
                    if p_re[j][0] in ['.', s[i]]:
                        dp_nex[j] = dp_nex[j] | dp[j - 1] if j - 1 >= 0 else dp_nex[j]
                        dp_nex[j] = dp_nex[j] | dp[j]
            dp = dp_nex

        # 结果
        return dp[-1]


if __name__ == "__main__":
    try1 = Solution()
    s = "aaa"
    p = "ab*ac*a"
    print(try1.isMatch(s, p))
