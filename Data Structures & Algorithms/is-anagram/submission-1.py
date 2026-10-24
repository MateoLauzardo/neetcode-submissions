class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap = {}
        hashmap2= {}

        #racecar
        for x in s: 
            if x not in hashmap:
                hashmap[x] = 1

            else:
                hashmap[x] += 1

        #carrace
        for j in t:
            if j not in hashmap2:
                hashmap2[j] = 1

            else:
                hashmap2[j] += 1


        return hashmap == hashmap2 

        