class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        while position:
            max_pos = max(position)
            time_for_max_position = (target-max_pos)/speed[position.index(max_pos)]#time for max position to reach target
            time = [(target - p) / s for p, s in zip(position, speed)]  
            i = 0
            while i < len(position):
                if time[i] <= time_for_max_position:
                   speed.pop(i)
                   position.pop(i)
                   time.pop(i)  # ✅ keep everything aligned
        # do NOT increment i here
                else:
                    i += 1  # ✅ only when you didn’t pop
            fleet += 1    
        return fleet

