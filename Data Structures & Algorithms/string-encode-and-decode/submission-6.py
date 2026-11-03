class Solution:

    def encode(self, strs: List[str]) -> str:

        # 5#Hello5#World
        string = ""

        for char in strs:
            string += str(len(char)) + "#" + char

        return string


    def decode(self, s: str) -> List[str]:

        answer = []

        i = 0 

        while i < len(s):

            j = i 

            while s[j] != "#":
                j += 1

            
            one = int(s[i]) #5
            two = j + 1
            end = one + two

            word = s[two:end]

            answer.append(word)

            i = end


        return answer 