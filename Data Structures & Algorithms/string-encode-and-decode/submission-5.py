class Solution:

    def encode(self, strs: List[str]) -> str:
        
        #5#hello5#world
        string = ""
        
        for char in strs:
            string += str(len(char)) + "#" + char

        return string


    def decode(self, s: str) -> List[str]:

        i = 0 

        answer = []

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1
            
            start = j + 1
            length = int(s[i:j])
            end = start + length

            answer.append(s[start:end])
            i = end 

        return answer 