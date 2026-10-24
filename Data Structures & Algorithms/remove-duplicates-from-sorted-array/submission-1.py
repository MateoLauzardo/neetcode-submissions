class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        
        #input: [1,1,2,3,4]


        #checks if list is empty 
        if not nums:
            return 0



        # pointer for the place to write unique elements
        write_index = 1

        # loop that starts from index 1 and goes up to the last index of the list nums
        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:

                nums[write_index] = nums[i]

                write_index += 1

        return write_index