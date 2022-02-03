# encoding:utf-8
# @Author :ZQY


# 参考官方答案的滑动窗口，自己写
"""
定义变量：
upper_cnt(list)大写字母位置，lower_cnt(list)小写字母位置
type_num设定的不区分大小写的字母种类
cnt大小写相同的字母种类
total当前不区分大小写的字母种类

伪代码：
for 循环每一个 type_num值
    for r <- 0 to end
        调整upper_cnt lower_cnt total cnt
        while total>type_num
            l向右移动
            调整upper_cnt lower_cnt total cnt
        这时total==type_num
        if cnt==total
            则找到完美字符串 return
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
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
