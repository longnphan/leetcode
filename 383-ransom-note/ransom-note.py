class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        def charMap(str):
            dict = {}
            for char in str:
                dict[char] = 1 + dict.get(char, 0)
            return dict

        ransom_map = charMap(ransomNote)
        magazine_map = charMap(magazine)

        for char in ransomNote:
            if ransom_map[char] > magazine_map.get(char, 0):
                return False
        
        return True