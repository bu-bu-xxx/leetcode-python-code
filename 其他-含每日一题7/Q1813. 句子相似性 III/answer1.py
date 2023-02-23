# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
import re


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = re.findall(r'(\S+)', sentence1)
        words2 = re.findall(r'[a-z,A-Z]+', sentence2)
        prefix = 0
        suffix = 0
        min_len = min(len(words1), len(words2))
        for i in range(min_len):
            if words1[i] == words2[i]:
                prefix += 1
            else:
                break

        for i in range(-1, -min_len - 1, -1):
            if words1[i] == words2[i]:
                suffix += 1
            else:
                break

        return (prefix + suffix) >= min_len


if __name__ == "__main__":
    try1 = Solution()
    sentence1 = "A A AAa"
    sentence2 = "A AAa"
    print(try1.areSentencesSimilar(sentence1, sentence2))
