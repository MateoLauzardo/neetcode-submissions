class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 2 hashmaps -> create two hashmaps one for s one for t

        hashmap1 = {} 
        hashmap2 = {}

        # hashmap1 = {r: 2, a: 2, c: 2, e: 1}
        for char in s:
            if char in hashmap1:
                hashmap1[char] += 1
            else:
                hashmap1[char] = 1

        # hashmap2 = {r: 2, a: 2, c: 2, e: 1} 
        for char in t:
            if char in hashmap2:
                hashmap2[char] += 1
            else:
                hashmap2[char] = 1


        return hashmap1 == hashmap2 
            
        
        


        