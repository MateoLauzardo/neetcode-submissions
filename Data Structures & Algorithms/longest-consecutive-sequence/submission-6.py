class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        



        # SECTION 1.)
        # {0, 3, 2, 5, 3, 6, 1}
        hashset = set()     

        for num in nums:
            hashset.add(num)


        # SECTION 2.)
        longest_sequence = 0 

        for num in hashset: 

            count = 1 
            current = num 

            if num - 1 not in hashset: 
                
                while current + 1 in hashset: 
                    current += 1 
                    count += 1

                longest_sequence = max(longest_sequence, count)

            
        
        return longest_sequence