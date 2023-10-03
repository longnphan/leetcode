class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in num_dict:
                return [num_dict[difference], i]
            else:
                num_dict[num] = i
