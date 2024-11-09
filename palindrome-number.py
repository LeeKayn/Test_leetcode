# Link https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)

        # Check if the string reads the same forwards and backwards
        return str_x == str_x[::-1]
