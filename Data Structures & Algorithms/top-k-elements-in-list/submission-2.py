class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
    

        # [(1, 1), (2, 2), (3, 3)]
        data = []
    
        for key, value in hashmap.items():
            heapq.heappush(data, (value, key))
            
            if len(data) > k:
                # heappop always removes the smallest value and automaically re-arranges itself
                heapq.heappop(data)


        
        answer = [] 
        for key, value in data:
            answer.append(value)

        
        return answer 
        
            
        


