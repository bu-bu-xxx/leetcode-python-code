# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，滑动窗口
import collections


class Solution:
    def balancedString(self, s: str) -> int:
        left, right = 0, 0
        res = 10 ** 6
        s_dict = collections.Counter(s)
        s_dict['Q'] = max(s_dict['Q'], 0)
        s_dict['W'] = max(s_dict['W'], 0)
        s_dict['E'] = max(s_dict['E'], 0)
        s_dict['R'] = max(s_dict['R'], 0)
        if len(set(s_dict.values())) == 1:
            return 0

        def check(l, r):
            return (r - l + 1) >= (max(s_dict.values()) * 4 - sum(s_dict.values()))

        for right in range(len(s)):
            s_dict[s[right]] -= 1
            if check(left, right):
                while left <= right:
                    s_dict[s[left]] += 1
                    left += 1
                    if not check(left, right):
                        res = min(res, right - left + 2)
                        break
                    else:
                        continue

        return res


if __name__ == "__main__":
    try1 = Solution()
    s = "QQQQ"
    print(try1.balancedString(s))
