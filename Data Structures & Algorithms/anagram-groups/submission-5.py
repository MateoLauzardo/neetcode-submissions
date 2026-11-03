class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}

        for char in strs:

            # your sorted word 
            reverse_word = "".join(sorted(char))

            # setting up list for each key 
            if reverse_word not in hashmap:
                hashmap[reverse_word] = []

            hashmap[reverse_word].append(char)


        answer = [] 

        for key, value in hashmap.items():
            answer.append(value)

        
        return answer 