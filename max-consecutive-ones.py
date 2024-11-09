# Link https://leetcode.com/problems/max-consecutive-ones/description/
# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # Initialize the count and max_count to 0
        count = 0
        max_count = 0

        # Iterate through the list of numbers
        for num in nums:
            # If the number is 1, increment the count
            if num == 1:
                count += 1
            # If the number is 0, update the max_count and reset the count
            else:
                max_count = max(max_count, count)
                count = 0

        # Update the max_count one last time
        max_count = max(max_count, count)

        return max_count