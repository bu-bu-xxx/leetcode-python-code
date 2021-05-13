# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


def lengthOfLongestSubstring(s):
    left = 0
    right = 1
    maxLen = 1
    if len(s) <= 1:
        maxLen = len(s)
    else:
        dict1 = {s[left]: 1}
        while right < len(s):
            if s[right] not in dict1:
                dict1[s[right]] = 1
                right = right + 1
                maxLen = max(maxLen, right - left)
            elif dict1[s[right]] == 0:
                dict1[s[right]] = 1
                right = right + 1
                maxLen = max(maxLen, right - left)
            else:
                dict1[s[left]] = 0
                left = left + 1
    return maxLen
