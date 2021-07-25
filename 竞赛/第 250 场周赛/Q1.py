# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5161. 可以输入的最大单词数


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        letters = list(brokenLetters)
        res = 0
        for word in words:
            if len(word) != 0:
                flag = True
                for letter in letters:
                    if letter in word:
                        flag = False
                if flag is True:
                    res += 1
        return res


if __name__ == "__main__":
    try1 = Solution()
    text1 = "hello world"
    brokenLetters1 = "ad"
    print(try1.canBeTypedWords(text1, brokenLetters1))
