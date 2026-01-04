class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        
        for n in nums:
            divisors = set()
            for i in range(1, int(n ** 0.5) + 1):  # Changed isqrt to n**0.5
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total
