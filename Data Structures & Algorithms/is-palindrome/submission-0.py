class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        forw = 0
        back = len(s)-1
        while (forw < back):

            if s[forw] != s[back]:
                return False
            else:
                forw +=1
                back -=1
        return True
                

        