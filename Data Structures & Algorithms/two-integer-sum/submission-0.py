class Solution:

    #given an array full of integers and a target. You should return a list 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #nums = [3,4,5,6], target = 7



        #create a hashmap  
        seen = {}

        for i, num in enumerate(nums):
            
            #complement is the number num (the number that is changing) needs to get 7
            complement = target - num

            #you are checking if its been spoted before 
            if complement in seen:
                #complement is the value not key, so doing this will return the key 
                return [seen[complement], i]

            seen[num] = i
            #First run: seen[3] = 0
            #output: {3 : 0}



        

     
