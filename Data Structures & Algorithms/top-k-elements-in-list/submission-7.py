class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1 

        heap = []

        # create a min heap
        for key, value in hashmap.items():
            
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

            
        
        answer = []

        for x in heap:
            answer.append(x[1])

        
        return answer 

            

