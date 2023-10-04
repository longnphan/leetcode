class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        maxCount = 0

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
            if count[num] > maxCount:
                result = num
                maxCount = count[num]
        return result