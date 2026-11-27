class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        if not nums:
            return 0

        # heap
        min_heap = []
        max_heap = []

        # min_heap[0] should be the lowest value
        for num in nums: 
            heapq.heappush(min_heap, num)

        # max_heap[0] should be the highest value value
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        lowest_value = min_heap[0] # 0 
        highest_value = -max_heap[0] # 10 
 

        # form the hashset -> {0, 3, 2, 5, 4, 6, 1, 1}
        hashset = set() 

        for num in nums:
            hashset.add(num)


        
        longest_sequence = 0 

        for num in hashset: 
            
            if num - 1 not in hashset:
                
                
                current = num
                count = 0 

                while current in hashset:
                    current += 1
                    count += 1

                longest_sequence = max(longest_sequence, count)

        
        return longest_sequence 
        

