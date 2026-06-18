class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A= []
        for index,number in enumerate(nums):
            A.append([number,index])
        A.sort()
        i =0
        j = len(nums)-1
        while i<j:
            if target == A[i][0]+A[j][0]:
                return [
                    min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])
                ]
            elif target > A[i][0]+A[j][0]:
                i = i+1
            elif target < A[i][0]+A[j][0]:
                j = j-1