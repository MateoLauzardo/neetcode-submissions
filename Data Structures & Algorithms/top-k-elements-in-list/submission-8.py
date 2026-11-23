class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # list [numbers]

        # return k amount of most frequent 

        # hashmap , key value (key = number) (value = instance)

        # min heap -> k being our condition 


        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        



        # min heap -> always keeps the samlles values at index 0 
        min_heap = []
    
        # tuple -> ( (value, key), (value, key) , (value, key)  )
        elements_tuple = ()

        for key, value in hashmap.items(): 
            

            elements_tuple = (value, key)

            if len(min_heap) < k:
                heapq.heappush(min_heap, elements_tuple)

            else:
                heapq.heappush(min_heap, elements_tuple)
                # removing index 0 cuz smallest value is at that index 
                heapq.heappop(min_heap)
            

        answer = [] 

        for x in min_heap:
            answer.append(x[1])

        
        return answer 