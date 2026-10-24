class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # 11#hello world2#hi
        string = ""

        for char in strs:
            string += str(len(char)) + "#" + char 
        return string 



    def decode(self, s: str) -> List[str]:
        array = [] 
        i = 0 

        while i < len(s):
            j = i 
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1 
            array.append(s[start:start + length]) # why so we add start + length


            i = j + 1 + length

        
        return array 
            
