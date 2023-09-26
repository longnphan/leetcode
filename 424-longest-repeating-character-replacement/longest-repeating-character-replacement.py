class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        result = 0
        p1 = 0

        for p2 in range(len(s)):
            char_dict[s[p2]] = 1 + char_dict.get(s[p2], 0)

            if (p2 - p1 + 1) - max(char_dict.values()) > k:
                char_dict[s[p1]] -= 1
                p1 += 1

            result = max(result, p2 - p1 + 1)
        return result