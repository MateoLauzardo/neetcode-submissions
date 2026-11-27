class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

 
        # {0, 3, 2, 5, 4, 6, 1}
        hashset = set()

        if not nums:
            return 0 

        # update hashset
        for num in nums:
            hashset.add(num)

        flag = 0 

        for value in hashset: 

            incremented_value = value + 1 

            if incremented_value in hashset:
                flag += 1

            
        return flag + 1 

        