# Link https://leetcode.com/problems/perfect-number/
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. A proper divisor is a positive integer that divides the number evenly, but is less than the number itself. Given an integer n, return true if n is a perfect number, otherwise return false.
# Example 1:
# Input: num = 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note that 28 is greater than the sum of its proper divisors, which is 1 + 2 + 4 + 7 = 14.

class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        sum_divisors = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i

        return sum_divisors == num