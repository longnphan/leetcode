class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map= {}

        for char in magazine:
            mag_map[char] = 1 + mag_map.get(char, 0)
        
        for char in ransomNote:
            if mag_map.get(char, 0):
                mag_map[char] = mag_map[char] - 1
            else:
                return False
        return True

