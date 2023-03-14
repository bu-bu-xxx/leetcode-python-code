# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        record = set()
        res = []
        for s in names:
            if s in record:
                for i in range(1, 10 ** 5):
                    if (tmp := s + "(" + str(i) + ")") in record:
                        continue
                    else:
                        record.add(tmp)
                        res.append(tmp)
                        break
            else:
                res.append(s)
                record.add(s)

        return res
