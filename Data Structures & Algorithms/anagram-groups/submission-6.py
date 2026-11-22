class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # hashmap 

        # sort the word (identfiying feature)

        # is that key in the hashmap, if not make it one and add said
        # value 

        # if it is, than just add value 

        # loop through hashmap.items, save them in its own list 


        # {sorted_word: ('tuple')}
        hashmap = {}

        for char in strs: 

            sorted_word = "".join(sorted(char))

            if sorted_word not in hashmap:
                hashmap[sorted_word] = []

            # we r trying to add the value to the tuple 
            hashmap[sorted_word].append(char)


        answer = [] 

        for key, tuple_value in hashmap.items():
            answer.append(tuple_value)

        
        return answer 

