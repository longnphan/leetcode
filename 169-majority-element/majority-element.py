class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        count = 0
        val = 0

        for num in nums:
            dict[num] = 1 + dict.get(num, 0)

            if dict[num] > count:
                count = dict[num]
                val = num
        return val