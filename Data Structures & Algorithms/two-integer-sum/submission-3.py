class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}

        for key, value in enumerate(nums):

            dif = target - value

            if dif in hashmap:
                answer = [key, hashmap[dif]]
                answer.sort()
                return answer  

            else:
                hashmap[value] = key 
        
        