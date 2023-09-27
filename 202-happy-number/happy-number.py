class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumNum(n)

            if n == 1:
                return True
        
        return False

    
    def sumNum(self, n):
        total_sum = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            total_sum += digit
            n = n // 10
        return total_sum