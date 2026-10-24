class Solution:
                    #use self for the first method of any class
                    #List[int] is a hint for the user to pass a list for the value "nums"
                    #bool is the same thing, should return True or False
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #creating hashSet
        seen = set()

        #[1, 2, 3, 3]
        for num in nums:
            
            if(num in seen):
                return True

            else:
                seen.add(num)

        return False








 

        