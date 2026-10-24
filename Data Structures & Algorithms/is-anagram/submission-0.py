class Solution:

    #your inputs are "s" and "t" which are both strings, and the output should be True or False
    def isAnagram(self, s: str, t: str) -> bool:
        
        #s = "racecar", t = "carrace"


        #create two hash maps, add the letters into each and check if letters are "in" each
        hashMap1 = {}

        hashMap2 = {}



        for letter in s:
             if letter in hashMap1:
                hashMap1[letter] += 1

             else:
                hashMap1[letter] = 1



        for letter in t:
             if letter in hashMap2:
                hashMap2[letter] += 1

             else:
                hashMap2[letter] = 1

        


        return hashMap1 == hashMap2



        

