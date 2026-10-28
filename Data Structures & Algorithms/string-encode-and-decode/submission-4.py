class Solution:

    def encode(self, strs: List[str]) -> str:

        # 5#hello5#world
        string = ""

        for char in strs:
            string += str(len(char))+"#"+ char
        
        return string 


    def decode(self, s: str) -> List[str]:

        answer = []

        i = 0 

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]

            answer.append(word)


            i = j + 1 + length
         

        return answer 