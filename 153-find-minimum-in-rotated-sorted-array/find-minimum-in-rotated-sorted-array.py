class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            if nums[p1] < nums[p2]:
                result = min(result, nums[p1])
                break

            mid = (p1 + p2) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[p1]:
                p1 = mid + 1
            else:
                p2 = mid - 1

        return result 