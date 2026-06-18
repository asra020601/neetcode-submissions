class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
           j = i+1
           c =0
           while j<len(temperatures):
               if temperatures[i]>temperatures[j] or temperatures[i]==temperatures[j]:
                  j =j+1
                  c = c+1
               else:
                  res.append(c+1)
                  break
               if j==len(temperatures):
                  res.append(0)
        res.append(0)
        return res