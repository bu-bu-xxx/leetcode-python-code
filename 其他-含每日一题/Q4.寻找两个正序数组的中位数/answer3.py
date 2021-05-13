# coding=utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 划分数组，然后进行二分法

def findMedianSortedArrays(nums1, nums2):
    # A长度小于等于B
    if len(nums1) <= len(nums2):
        A, B = nums1, nums2
    else:
        B, A = nums1, nums2

    infinity = 2 ** 20
    m, n = len(A), len(B)

    # 特殊情况A为空集
    if m == 0:
        val = (B[n//2]+B[(n-1)//2])/2
        return val

    # 验证取A[i]和B[j]能否满足A[i-1]<=B[j]，默认有i-1和i和j-1和j
    def check(i):
        j = (m + n + 1) // 2 - i
        A_i1 = (-infinity if i == 0 else A[i - 1])
        B_j = (infinity if j == n else B[j])
        return A_i1 <= B_j

    # 二分法查询A
    left = 0
    right = m
    while left < right:
        if left == right - 1:
            left = (right if check(right) else left)
            break
        mid = (left + right) // 2
        left, right = (mid, right) if check(mid) else (left, mid)

    # 计算中位数
    # 特殊情况，中位数不在A里面
    ji_ou = (m + n) % 2
    note = (m+n+1)//2-left

    A_left1 = -infinity if left == 0 else A[left-1]
    A_left = infinity if left == m else A[left]
    B_left1 = -infinity if note == 0 else B[note - 1]
    B_left = infinity if note == n else B[note]
    val = max(A_left1,B_left1) if ji_ou else \
        (max(A_left1,B_left1)+min(A_left,B_left))/2
    return val


if __name__ == '__main__':
    nums1 = [10000]
    nums2 = [10001]
    print(findMedianSortedArrays(nums1,nums2))