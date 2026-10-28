class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        

        my_heap = []


        for key, value in hashmap.items():

            # [(1:1), (2:2), (3:3)]
            heapq.heappush(my_heap, (value, key))

            # [(2:2), (3:3)]
            if len(my_heap) > k:
                heapq.heappop(my_heap)

            
        answer = [] 


        for x in my_heap:
            answer.append(x[1])


        return answer 
        