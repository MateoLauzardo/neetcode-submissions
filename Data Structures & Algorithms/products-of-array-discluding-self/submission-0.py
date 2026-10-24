class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n  # Start with [1, 1, 1, 1]

        # Step 1: Left pass – product of all elements to the left of each index
        left = 1
        for i in range(n):
            answer[i] = left        # Set current index to running left product
            left *= nums[i]         # Update left with current number

        # At this point:
        # nums    = [1, 2, 3, 4]
        # answer  = [1, 1, 2, 6]

        # Step 2: Right pass – multiply by product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):  # Loop from last index to 0
            answer[i] *= right         # Multiply current value by right product
            right *= nums[i]           # Update right with current number

        # Final answer = [24, 12, 8, 6]
        return answer

        


        
