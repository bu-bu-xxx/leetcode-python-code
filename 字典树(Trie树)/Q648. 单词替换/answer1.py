# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
import re
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = re.findall(r'[a-z]+',sentence)
        for idx,word in enumerate(words):
            for i in range(len(word)):
                if word[:i+1] in dictionary:
                    words[idx] = word[:i+1]
                    break
        return ' '.join(words)
