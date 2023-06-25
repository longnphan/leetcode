class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            "}":"{",
            ")": "(",
            "]": "["}

        char_stack = []

        for char in s:
            if char in char_dict:
                if len(char_stack) == 0:
                    return False
                elif char_dict[char] == char_stack[-1]:
                    char_stack.pop()
                else:
                    return False

            else:
                char_stack.append(char)
        
        return len(char_stack) == 0
                
