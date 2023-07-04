class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def charMap(word):
            dict = {}
            for letter in word:
                dict[letter] = 1 + dict.get(letter, 0)
            return dict
        
        sMap = charMap(s)
        tMap = charMap(t)
        
        for char in tMap:
            if sMap.get(char, 0) != tMap[char]:
                return char