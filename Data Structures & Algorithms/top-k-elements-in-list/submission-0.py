from typing import List  # Required for type hints

class Solution:

    # Given a list of ints and an int k, return the k most frequent elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequencies using hashMap
        hashMap = {}

        for i in nums:
            if i in hashMap:
                hashMap[i] += 1

            else:
                hashMap[i] = 1

        #hashMap = {
            #1: 3,
            #2: 2,
            #3: 1
        #}

#-----------------------------------------------------------------------------------------------------
       
        # Step 2: Create buckets — index = frequency, value = list of numbers
        buckets = []

        for j in range(len(nums) + 1):
            buckets.append([])
            #[] [] [] [] [] []


        # Step 3: Place numbers into the correct bucket based on frequency
        for num, freq in hashMap.items():
            buckets[freq].append(num)
            #The bucket at the highest index has the numbers with the highest frequency.


            
        #[],      # index 0 — no number appears 0 times
        #[3],     # index 1 — number 3 appeared once
        #[2],     # index 2 — number 2 appeared twice
        #[1],     # index 3 — number 1 appeared three times
        #[], [], []

#-----------------------------------------------------------------------------------------------------

        result = []

        # Start from the highest frequency down to 1
                          
                          #start = 6   #0 = stop,  #-1 = go back one at a time 
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                #if length of result / which is empty in the beggining but adds as time moves
                #than return and stop loop
                if len(result) == k:
                    return result











        