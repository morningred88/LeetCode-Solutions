"""
Problem 1: Two Sums
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.


Link to the solution:
https://dev.to/xshirl/two-sum-leetcode-3afp

"""

from typing import List


class Solution11:

    # O(n^2) time, O(1) space
    # Use two pointers(for loops) to loop through the array and find the indices of the two numbers
    # that add up to the target number.
    def two_Sum_brute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number_to_find = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == number_to_find:
                    return [i, j]

    # O(n) time, O(n) space
    # Using hash table to store the numbers as key and indices as value.
    # Then check if the number to find is in the hashtable
    # If the number to find is in hashtable, then return both the index of the number and number to find
    def two_sum_hash(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}
        for i in range(len(nums)):
            number_to_find = target - nums[i]
            if number_to_find in nums_map:
                return [i, nums_map[number_to_find]]
            else:
                nums_map[nums[i]] = i


solution = Solution11()
print(solution.two_Sum_brute([1, 3, 5, 7, 2], 9))
print(solution.two_sum_hash([1, 3, 5, 7, 2], 9))
