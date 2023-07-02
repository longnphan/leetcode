class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        arr = [[] for i in range(len(nums) + 1)]
        i = k
        
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        
        for num, count in dict.items():
            arr[count].append(num)
                
        result = []
        
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res