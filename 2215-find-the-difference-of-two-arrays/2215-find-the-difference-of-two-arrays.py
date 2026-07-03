class Solution:
    def findDifference(self, nums1, nums2):

        A = set(nums1)
        B = set(nums2)

        return [list(A-B), list(B-A)]