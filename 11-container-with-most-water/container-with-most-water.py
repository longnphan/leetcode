class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_idx, right_idx = 0, len(height) - 1

        while left_idx < right_idx:
            area = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
            max_area = max(max_area, area)

            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -=1
                
        return max_area