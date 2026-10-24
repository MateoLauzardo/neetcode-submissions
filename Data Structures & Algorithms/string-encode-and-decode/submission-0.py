class Solution:

    def encode(self, strs: List[str]) -> str:

        #["neet","code","love","you"]

        s = ""

        for string in strs:

          s += str(len(string)) + "#" + string
        
        return s

        #output: 4#neet4#code4#love3#you




                    #made our output 's' so we can call it here
    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != '#':
                j += 1

                        #slicing "start from i" get everything before "j"
            length = int(s[i:j])
                        #adds everything before 6 
            word = s[j + 1 : j + 1 + length]
                        #2 : 2 + 4
            res.append(word)

            i = j + 1 + length
            #I = 1 + 1 + 4

        return res










