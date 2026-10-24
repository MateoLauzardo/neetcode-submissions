class Solution:
                        #given "strs" which is a list of strings. 
                        #should output a list full of other list's that have strings in them 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        #multiple of the same letter, so you have to use hashmap 
        hashMap = {}



        #["act","pots","tops","cat","stop","hat"]
        for word in strs:
            
                            #sorted gets the letters and puts each one in a list. the 
                            #.join method is what makes it back to a string
            key = "".join(sorted(word)) 

            if key not in hashMap:
                hashMap[key] = []

            
            hashMap[key].append(word) 


            #the list part converts whatever inside into a list 
                    #this gets values from hashmap
        return list (hashMap.values())




           



        