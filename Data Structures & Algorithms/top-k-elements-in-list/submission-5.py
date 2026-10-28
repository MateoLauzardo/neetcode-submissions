class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1   

            
        
        # create a min heap    
        heap = []

        for key, value in hashmap.items():
            
            # always be adding the next value 
            heapq.heappush(heap, (value, key))

            # if heap is every greatern than pop the smallest value 
            if len(heap) > k:
                heapq.heappop(heap)

            



        # heap -> # {2:2, 3:3}
        answer = []

        for char in heap:
            number = char[1]

            answer.append(number)


        return answer 
            

            


