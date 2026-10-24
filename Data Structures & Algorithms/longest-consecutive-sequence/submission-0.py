class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums) #adds values into hashset 
        longest = 0

        for num in hashset:

            if num - 1 not in hashset:  # start of a sequence
                length = 1
                current = num


                while current + 1 in hashset:
                    current += 1
                    length += 1


                longest = max(longest, length)


        return longest


            
            

