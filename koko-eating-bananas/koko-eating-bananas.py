class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftIdx, rightIdx = 1, max(piles)
        res = max(piles)

        while leftIdx <= rightIdx:
            k = (leftIdx + rightIdx) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)
            if totalTime <= h:
                res = min(res, k)
                rightIdx = k - 1
            else:
                leftIdx = k + 1
        return res