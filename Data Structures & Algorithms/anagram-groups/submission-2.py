class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # {'act': 'cat', 'opst': 'stop', 'aht': 'hat'}

        hashmap = {}

        for char in strs:
            
            sorted_text = ''.join(sorted(char))
            
            
            # add for FIRST time 
            if sorted_text not in hashmap:
                hashmap[sorted_text] = []  

            # add ANOTHER char 
            hashmap[sorted_text].append(char)
            

        return list(hashmap.values())
 




    
        