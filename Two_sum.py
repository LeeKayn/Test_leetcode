# Link https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the indices of the elements
        num_to_index = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If it exists, return the indices
                return [num_to_index[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i
