class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []

        for val in s:
            if val == "[" or val == "(" or val == "{":
                stack.append(val)
            else:
                if stack and valid[val] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
        
        if not stack:
            return True
        
        return False


# (){[]}