class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':  # check if length of integer > 1 
                j += 1
            length = int(s[i:j])

            i = j+1
            ans.append(s[i:i+length])
            i += length
        return ans