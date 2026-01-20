def intersection(nums1, nums2):
    lst = []
    for num in nums1:
        if num in nums2:
            lst.append(num)

    return list(set(lst))


nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1,nums2))