class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        #[3,4,5,6]
        for x, j in enumerate(nums):
            comp = target - j 
            

            if comp not in hashmap:
                hashmap[j] = x

            else:
                return[hashmap[comp], x]
        