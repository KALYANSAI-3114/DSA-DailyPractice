def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        temp +=nums2[:n]
        temp = sorted(temp)
        for i in range(m+n):
            nums1[i] = temp[i]

        return nums1
    
nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n= 3
print(merge(nums1,m,nums2,n))