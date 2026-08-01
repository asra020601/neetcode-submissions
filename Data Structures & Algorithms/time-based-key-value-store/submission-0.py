class TimeMap:
    def __init__(self):
        #we need a dictionary to store these keys and values
        self.dict1={}
        #but how do i track timestamp?
    def set(self, key: str, value: str, timestamp: int) -> None:
        #put one key and two dimesional values
        #{"key":[["value"],[timestamp]]}
        if key in self.dict1.keys():#if the key already exists we just append to it
           self.dict1[key].append([value,timestamp])
        else:
           self.dict1[key]=[[value,timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1: return ""
      
        #we need the timestamp closest to the given timestamp
        l,r = 0,len(self.dict1[key])-1
        res = ""
        while l<=r:
          mid = (l+r)//2
          if timestamp==self.dict1[key][mid][1]:
            return self.dict1[key][mid][0]
          elif timestamp<self.dict1[key][mid][1]:
           
            r = mid-1
          elif timestamp>self.dict1[key][mid][1]:
            res = self.dict1[key][mid][0]
            l = mid+1
          
        
        return res