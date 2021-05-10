# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 中心扩展，动态规划
# 状态转移函数
# P(i,i)=True
# P(i,i+1)=(Si == Si+1)
# P(i,j) = P(i+1,j-1) and (Si == Sj)
# 搜寻长度为1和2的字符串，找到最大的回文长度
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)

        def S(i, j):
            return s[i] == s[j]

        # 给两个初始位置，得到最大回文数，和位置
        def check(*ad):
            if len(ad) == 1:
                i, j = ad[0], ad[0]
            else:
                i, j = ad[0], ad[1]
            while i >= 0 and j < s_len:
                if S(i, j):
                    i -= 1
                    j += 1
                else:
                    break
            all_len = j - i - 1
            return all_len, i + 1, j - 1

        max_len = []
        i_set = []
        j_set = []

        # 全部搜寻
        for tag in range(s_len - 1, -1, -1):
            max_len.append(check(tag)[0])
            i_set.append(check(tag)[1])
            j_set.append(check(tag)[2])
        for tag in range(s_len - 2, -1, -1):
            max_len.append(check(tag, tag + 1)[0])
            i_set.append(check(tag, tag + 1)[1])
            j_set.append(check(tag, tag + 1)[2])
        # 比较
        max_ad = 0
        max_val = max_len[0]
        for tag in range(len(max_len)):
            if max_len[tag] > max_val:
                max_val = max_len[tag]
                max_ad = tag

        return s[i_set[max_ad]:j_set[max_ad] + 1]


if __name__ == '__main__':
    try1 = Solution()

    s = "ccc"
    print(try1.longestPalindrome(s))
