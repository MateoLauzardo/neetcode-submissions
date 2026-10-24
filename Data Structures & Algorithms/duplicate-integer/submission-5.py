class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # make a hashmap 
        # loop through the list 
        # once ur hashmap full you are going to check if there r dup

        hashmap = {}


        for num in nums:
            if num in hashmap:
                # [1:1, 2:1, 3:2]
                return True
            else:
                hashmap[num] = 1

        return False 

        

        