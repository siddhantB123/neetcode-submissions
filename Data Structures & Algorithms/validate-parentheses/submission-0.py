class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping.values():  # opening brackets
                stack.append(ch)
            elif ch in mapping:  # closing brackets
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                # invalid character
                return False
        
        return not stack

        