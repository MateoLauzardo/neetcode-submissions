class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # how do we sort this 

        # hashset = ()

        # add all thes values 

        # flag

        # loop through hashmap if that value += 1
        # in hashmap, if it is, increamtenet flag by one 
        # and continue 

        # return flag 


        # {0, 3, 2, 5, 4, 6, 1}
        hashset = set()

        # update hashset
        for num in nums:
            hashset.add(num)

        flag = 0 

        for value in hashset: 

            incremented_value = value + 1 

            if incremented_value in hashset:
                flag += 1

            
        return flag + 1 

        