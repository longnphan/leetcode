class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left, right = 0, len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        str = list(s)
        

        while left < right:
            if str[left] in vowels and str[right] in vowels:
                str[left], str[right] = str[right], str[left]
                left += 1
                right -= 1
            else:
                if str[left] not in vowels:
                    left += 1
                if str[right] not in vowels:
                    right -= 1

        return "".join(str)