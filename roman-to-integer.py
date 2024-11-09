# Link https://leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Example 1:
# Input: "III"
# Output: 3
# Example 2:
# Input: "IV"
# Output: 4
# Example 3:
# Input: "IX"
# Output: 9


class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to store the values of the Roman numerals
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the result to 0
        result = 0

        # Iterate through the string
        for i in range(len(s)):
            # Get the value of the current Roman numeral
            value = roman_to_int[s[i]]

            # If the next Roman numeral is greater than the current one, subtract the current value
            if i + 1 < len(s) and roman_to_int[s[i + 1]] > value:
                result -= value
            # Otherwise, add the current value
            else:
                result += value

        return result