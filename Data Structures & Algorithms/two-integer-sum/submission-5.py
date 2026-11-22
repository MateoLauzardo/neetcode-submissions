class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap 

        # dif -> target - nums 

        # if that value is in the hashmap already 

        hashmap = {} 

        for key, value in enumerate(nums):

            dif = target - value 

            if dif in hashmap: 
                return [hashmap[dif], key] 
            
            else:
                hashmap[value] = key             
        