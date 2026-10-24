class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #given a list of ints called "nums" and a int called "val"
        #we need to remove all occurences of val from list 

        # [0,1,2,2,3,0,4,2]
        # val = 2
        pointer = 0

        #this makes i an index, allow our if statement to work
        for i in range(len(nums)):

            if nums[i] != val:

                nums[pointer] = nums[i]

                pointer += 1

        return pointer 
