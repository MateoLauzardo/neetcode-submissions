class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left_array  = [1,  1,  2, 8]
        # right_array = [48, 24, 6, 1]
        # result      = [48, 24, 12, 8]

        n = len(nums)
        left_array = [0] * n # [1,1,2,8]
        right_array = [0] * n # [48, 24, 6, 1]

        # Loop 1: left_array[i] = product of everything before i
        left_mult = 1
        for i in range(n):
            left_array[i] = left_mult
            left_mult *= nums[i]

        # Loop 2: right_array[i] = product of everything after i
        right_mult = 1
        for i in range(n - 1, -1, -1):
            right_array[i] = right_mult
            right_mult *= nums[i]

        # Combine them
        answer = []

        for i in range(n):
            answer.append(left_array[i] * right_array[i])

        return answer 