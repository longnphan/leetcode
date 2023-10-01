class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        l = 0

        for r in range(len(arr)):
            if arr[r] == " " or r == len(arr) - 1:
                temp_l = l
                temp_r = r - 1

                if r == len(arr) - 1:
                    temp_r = r
                while temp_l < temp_r:
                    arr[temp_l], arr[temp_r] = arr[temp_r], arr[temp_l]
                    temp_l += 1
                    temp_r -= 1

                l = r + 1
        
        return "".join(arr)