# encoding:utf-8
# @Author :ZQY


# 把answer1和answer2合并


class Solution:
    def longestNiceSubstring1(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << ord(s[j]) - ord('a')
                else:
                    upper |= 1 << ord(s[j]) - ord('A')
                if len(res) < (j - i + 1) and lower == upper:
                    res = s[i:j + 1]

        return res

    def longestNiceSubstring2(self, s: str) -> str:
        type_num_max = 26
        res_l, res_len = 0, 0

        for type_num in range(1, type_num_max):
            upper_cnt, lower_cnt = [0] * 26, [0] * 26
            same_cnt, total, l, r = 0, 0, 0, 0
            for r in range(len(s)):
                # 调整数值
                tmp = ord(s[r].lower()) - ord('a')
                if s[r].isupper():
                    upper_cnt[tmp] += 1
                    if upper_cnt[tmp] == 1 and lower_cnt[tmp] >= 1:
                        same_cnt += 1
                    if upper_cnt[tmp] == 1 and lower_cnt[tmp] == 0:
                        total += 1
                else:
                    lower_cnt[tmp] += 1
                    if lower_cnt[tmp] == 1 and upper_cnt[tmp] >= 1:
                        same_cnt += 1
                    if lower_cnt[tmp] == 1 and upper_cnt[tmp] == 0:
                        total += 1
                while total > type_num:
                    # 调整数值
                    tmp = ord(s[l].lower()) - ord('a')
                    if s[l].isupper():
                        upper_cnt[tmp] -= 1
                        if lower_cnt[tmp] >= 1 and upper_cnt[tmp] == 0:
                            same_cnt -= 1
                        if lower_cnt[tmp] == 0 and upper_cnt[tmp] == 0:
                            total -= 1
                    else:
                        lower_cnt[tmp] -= 1
                        if upper_cnt[tmp] >= 1 and lower_cnt[tmp] == 0:
                            same_cnt -= 1
                        if upper_cnt[tmp] == 0 and lower_cnt[tmp] == 0:
                            total -= 1
                    l += 1

                # 判断
                if same_cnt == total and same_cnt == type_num:
                    if (r - l + 1) > res_len:
                        res_len, res_l = r - l + 1, l

        # 输出
        return s[res_l:res_l + res_len]

    def longestNiceSubstring(self, s: str) -> str:
        if len(s) >= 26 * 2:
            return self.longestNiceSubstring2(s)
        return self.longestNiceSubstring1(s)
