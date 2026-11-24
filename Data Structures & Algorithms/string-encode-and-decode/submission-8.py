class Solution:
    

    # strs: ["Hello","World"]  -> return "Hello World"
    def encode(self, strs: List[str]) -> str:
        
        # 5#Hello5#World
        string = ""

        for word in strs: 
            string += str(len(word))
            string += "#" 
            string += word 
        
        return string 
        

    def decode(self, s: str) -> List[str]:
        
        answer = [] 

        start = 0 
        i = 0 


        while start < len(s):

            while s[start] != "#":
                start += 1

            length = int(s[i:start])
            start += 1
            combined_length = length + start 

            word = s[start:combined_length]

            answer.append(word)

            start = combined_length
            i = start
 

        return answer 
