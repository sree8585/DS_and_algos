class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)

        left = 0
        right = n1

        while (left <= right):
            partitionNum1 = (left + right) // 2
            partitionNum2 = ((n1 + n2 + 1) // 2) - partitionNum1
            # if partitionN1 is 0 it means nothing is there on left side.Use -INF for maxNums1_L
            # if partitionN2 is length of input then there is nothing on right side.Use +INF for minNums1_R
            maxNums1_L = float("-inf") if partitionNum1 == 0 else nums1[partitionNum1-1]
            minNums1_R = float("inf") if partitionNum1 == n1 else nums1[partitionNum1]

            maxNums2_L = float("-inf") if partitionNum2 == 0 else nums2[partitionNum2 - 1]
            minNums2_R = float("inf") if partitionNum2 == n2 else nums2[partitionNum2]

            if (maxNums1_L <= minNums2_R) and (minNums1_R >= maxNums2_L):
                # We have found the right place
                if (n1 + n2) % 2 == 0:
                    return (max(maxNums1_L, maxNums2_L) + min(minNums1_R, minNums2_R)) / 2
                else:
                    return max(maxNums1_L, maxNums2_L)
            elif maxNums1_L > minNums2_R:
                # We need to move left on nums1
                right = partitionNum1 - 1
            else:
                # We need to move right nums1, which invariably will push the pinter to the left on nums2
                left = partitionNum1 + 1






