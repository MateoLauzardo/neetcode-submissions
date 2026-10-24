class Solution:
    #s = "Was it a car or a cat I saw?"
    def isPalindrome(self, s: str) -> bool:

        #gets string, makes everything lower and all one thing
        cleaned = []

        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())

        s = ''.join(cleaned)
        # s = wasitacaroracatisaw
#----------------------------------------------------------

        pointer = len(s) - 1

        for i in range(len(s) // 2):
            if s[i] != s[pointer]:
                return False 
            
            pointer -= 1

        return True 


        