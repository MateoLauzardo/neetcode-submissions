class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hash set -> loop through nums, any instance if cant 
        #             append to hashset, return True  
         

        # hashmap -> loop through nums, loop through hashmap
        #            if value in key > 2 obv return True 
        
        hashset = set() 

        for num in nums:

            if num in hashset:
                return True 
            else:
                hashset.add(num)

        return False 

        