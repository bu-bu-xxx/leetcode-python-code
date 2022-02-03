# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 把字典换成可变集合set，效率稍微高一点
def lengthOfLongestSubstring(s):
    left = 0
    right = 1
    maxLen = 1
    if len(s) <= 1:
        maxLen = len(s)
    else:
        Set = set(s[left])
        while right < len(s):
            if s[right] not in Set:
                Set.add(s[right])
                right = right + 1
                maxLen = max(maxLen, right - left)
            else:
                Set.remove(s[left])
                left = left + 1
    return maxLen
