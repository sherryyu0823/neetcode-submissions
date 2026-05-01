class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        if m>n:
            A, B = B, A
            m, n = n, m
        
        l, r = 0, m
        half = (m+n+1)//2

        while l<=r:
            mid = (l+r)//2
            if mid-1>=0:
                left_a = A[mid-1]
            else:
                left_a = float("-inf")
            
            if mid < m:
                right_a = A[mid]
            else:
                right_a = float("inf")
        
            mid_b = half-mid
            
            if mid_b-1>=0:
                left_b = B[mid_b-1]
            else:
                left_b = float("-inf")
            
            if mid_b < n:
                right_b = B[mid_b]
            else:
                right_b = float("inf")

            if left_a<=right_b and right_a>=left_b:

                if (m+n)%2 == 0:
                    return ((max(left_a, left_b)+min(right_a, right_b))/2)
                else:
                    return max(left_a, left_b)
            
            if left_a > right_b:
                r = mid-1
            elif right_a < left_b:
                l = mid+1