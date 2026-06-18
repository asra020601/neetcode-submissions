class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i,j  = 0,0
        while i<len(nums1) and j<len(nums2):
            min_val = min(nums1[i],nums2[j])
            if nums1[i]==min_val:
                res.append(nums1[i])
                i = i+1
            else:
                res.append(nums2[j])
                j = j+1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        if len(res)%2!=0:
          return (res[(len(res)//2)])
        else:
          mid = (res[(len(res)//2)] +res[((len(res)//2)-1)])/2
          return (mid)
