class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            mid =  numbers[i]+numbers[j]
            if target == mid:
                return ([i+1,j+1])
                
            elif target > mid:
                i =i +1
            elif target < mid:
                j =  j-1