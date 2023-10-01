class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left_idx = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left_idx], nums[i] = nums[i], nums[left_idx]
                left_idx += 1
            
        return nums