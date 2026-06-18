class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            j = i+1
            index_of_warmer_day= 0
            while j<len(temperatures):
                  if temperatures[i]<temperatures[j]:
                     res[i]=j-i
                     break
                  else:
                      j = j+1
        return res