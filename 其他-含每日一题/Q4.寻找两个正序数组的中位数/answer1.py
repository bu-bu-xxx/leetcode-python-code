# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己的报错

# 二分法
def findMedianSortedArrays(nums1, nums2):
    # 去除AB列表前共k个项
    n = len(nums1) + len(nums2)
    if n % 2 == 0:  # 偶数
        k = n / 2 - 1
        jiou = 0
    if n % 2 == 1:  # 奇数
        k = n // 2
        jiou = 1
    # AB有空集的情况
    if len(nums1) == 0:
        if jiou == 0:
            return (nums2[k] + nums2[k + 1]) / 2
        if jiou == 1:
            return nums2[k]
    if len(nums2) == 0:
        if jiou == 0:
            return (nums1[k] + nums1[k + 1]) / 2
        if jiou == 1:
            return nums1[k]

    # AB没空集的情况
    a = 0
    b: int = 0  # 去除后的数组开头指针
    kk = k  # kk迭代
    while k > 0:
        if k == 1:
            if nums1[a] < nums2[b]:
                a = a + 1
            else:
                b = b + 1
            break
        # 第一步，分两种情况去除AB的k/2
        if k != 1:

            kk = k // 2
            aa = min(a + kk, len(nums1))
            bb = min(b + kk, len(nums2))


        if nums1[a] >= nums2[b]:
            b = bb
        else:
            a = aa

        # 第二步，更新k
        k = k - a - b
        if aa == len(nums1):  # 如果一个数组全部过滤完
            b = b + kk
            break
        if bb == len(nums2):
            a = a + kk
            break
    # 第三步，判断是否去除k个

    # 第四步，返回结果
    if jiou == 0:
        if a == len(nums1):
            return (nums2[b] + nums2[b + 1]) / 2
        if b == len(nums2):
            return (nums1[a] + nums1[a + 1]) / 2
        return (nums1[a] + nums2[b]) / 2
    if jiou == 1:
        if a == len(nums1):
            return nums2[b]
        if b == len(nums2):
            return nums1[a]
        return min(nums1[a], nums2[b])


if __name__ == '__main__':
    nums1 = [0,0,0,0,0]
    nums2 = [-1,0,0,0,0,0,1]
    print(findMedianSortedArrays(nums1,nums2))