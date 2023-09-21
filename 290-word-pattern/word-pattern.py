class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        s = s.split(" ")

        if len(pattern) != len(s):
          return False

        for i, letter in enumerate(pattern):
          if letter not in dict:
            if s[i] not in dict.values():
              dict[letter] = s[i]
            else:
              return False
          elif dict[letter] != s[i]:
              return False
        
        return True