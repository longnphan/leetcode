class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        needleLen = len(needle)

        while needleLen <= len(haystack):
            currNeedle = haystack[i : needleLen]
            if currNeedle == needle:
                return i
            i += 1
            needleLen += 1
        return -1