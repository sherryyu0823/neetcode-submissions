class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = []
        clean = []
        for c in s:
            if c.isalnum():
                clean.append(c.lower())
        for i in range(len(clean)-1, -1, -1):
            ss.append(clean[i])
        
        clean = "".join(clean)
        new = clean[::-1]
        if new==clean:
            return True
        else:
            return False
