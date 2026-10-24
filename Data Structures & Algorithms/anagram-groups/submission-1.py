class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for x in strs: 
            key = "".join(sorted(x))

            if key not in hashmap: 
                hashmap[key] = []

            hashmap[key].append(x)

        return list(hashmap.values())

        