class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            difference = numbers[l] + numbers[r]

            if difference == target:
                return [l+1, r+1]
            elif difference < target:
                l += 1
            else:
                r -= 1
            