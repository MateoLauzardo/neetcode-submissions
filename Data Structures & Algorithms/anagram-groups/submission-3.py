class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = []
        hashmap = {}

        # loop through strs 
        # sort that word 
        # if that word is not in hashmap hashmap[word] = []
        # if that word is in append to the array 

        for string in strs:

            sorted_word = "".join(sorted(string))

            if sorted_word not in hashmap:
                hashmap[sorted_word] = []

            hashmap[sorted_word].append(string)

        for key, value in hashmap.items():
            answer.append(value)

        return answer 
        