# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a1, b1):
            n = len(a1)
            if n % 2 == 1:
                left = n // 2 - 1
                right = n // 2 + 1
            else:
                left = n // 2 - 1
                right = n // 2

            while left >= 0:
                if a1[left] == a1[right]:
                    left -= 1
                    right += 1
                    continue
                else:
                    if b1[:left + 1] == a1[right:][-1::-1] or \
                            a1[:left + 1] == b1[right:][-1::-1]:
                        return True
                    else:
                        return False

            return True

        return check(a, b) or check(b, a)
