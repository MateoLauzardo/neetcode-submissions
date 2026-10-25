class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # {1:1, 2:2, 3:3}
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1


        min_heap = [] 

        # while loop
        # if len of heap is greater than k
        # heappush[0]
        # makes sure highest values are stored 
        


        # adding the first two keys 
        for key, value in hashmap.items():

            if len(min_heap) < k:
                
                heapq.heappush(min_heap, (value, key))


            else:
                # removes smallest value and add new value 
                if min_heap[0][0] < value:
                    # than pop first value of heap
                    heapq.heappop(min_heap)
                    # than add new value to heap
                    heapq.heappush(min_heap, (value, key))


        answer = []

        for x in min_heap:
            answer.append(x[1])

        return answer 