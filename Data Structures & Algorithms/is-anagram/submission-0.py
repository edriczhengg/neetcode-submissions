class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for let in s:
            if let in counts:
                counts[let] += 1
            else:
                counts[let] = 1

        for let2 in t:
            if let2 in counts:
                counts[let2] -= 1
        
        for val in counts.values():
            if val != 0:
                return False
        
        return True
        
    



