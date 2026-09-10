class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,number in enumerate(nums):
            component = target-number
            if component in hashmap:
                return[hashmap[component],index]
            hashmap[number]=index
    