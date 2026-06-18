class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i<len(numbers):
           var1 = numbers[i]
           var2 = target-var1
           if var2 in numbers and numbers.index(var2)!=i:
              return [i+1,numbers.index(var2)+1]
              break
           else:
             i = i+1
