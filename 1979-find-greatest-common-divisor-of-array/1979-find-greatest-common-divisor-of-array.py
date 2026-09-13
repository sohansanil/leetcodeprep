class Solution:
    def findGCD(self, nums):

        divisor = min(nums)
        dividend = max(nums)

        while dividend % divisor != 0 :
            temp = dividend
            dividend = divisor
            divisor = temp % dividend
        return divisor