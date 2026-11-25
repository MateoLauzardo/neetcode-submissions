class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # technique: prefix and suffix tech 
        
        L = len(nums)
        left_array = [0] * L # [0, 0, 0, 0]
        right_array = [0] * L # [0, 0, 0, 0]

        # left_array = [1, 1, 2, 8]
        left = 1 
        for i in range(L):
            left_array[i] = left
            left *= nums[i]   

        # right_array = [48, 24, 6, 1]
        right = 1 
        for i in range(L-1, -1, -1): 
            right_array[i] = right
            right *= nums[i]  

        output = [] 

        for x in range(L):
            output.append(left_array[x] * right_array[x])

        return output 





        