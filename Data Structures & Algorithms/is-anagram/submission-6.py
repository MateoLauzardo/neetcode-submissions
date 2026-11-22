class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap1 = {}

        hashmap2 = {}

        for char in s:
            
            if char not in hashmap1:
                hashmap1[char] = 1
            else:
                hashmap1[char] += 1

            
        for char in t:
            
            if char not in hashmap2:
                hashmap2[char] = 1
            else:
                hashmap2[char] += 1


        return hashmap1 == hashmap2 