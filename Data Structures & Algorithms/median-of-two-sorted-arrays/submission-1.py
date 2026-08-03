class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leftsize = ((len(nums1)+len(nums2))+1)//2
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1 #exchange them becasue we also assume that nums1 is smaller
        l,r =0,len(nums1)
        while l<=r:
            i=(l+r)//2
            j = leftsize-i
            aleft = nums1[i-1] if i>0 else float('-inf')
            bleft = nums2[j-1] if j>0 else float('-inf')
            aright = nums1[i] if i<len(nums1) else float('inf')
            bright = nums2[j] if j <len(nums2) else float('inf')
            if aleft<=bright and bleft<=aright:
                if (len(nums1)+len(nums2))%2:
                    return max(aleft,bleft)
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2
            elif aleft>bright:
                r=i-1
            else:
                l=i+1
        