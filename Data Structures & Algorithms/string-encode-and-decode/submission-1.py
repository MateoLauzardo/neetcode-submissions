class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        array = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":      # find the end of the number
                j += 1

            length = int(s[i:j])    # the number before the #
            start = j + 1           # string starts right after #
            array.append(s[start:start + length])

            i = start + length      # jump to the next length

        return array