"""
Problem #283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

from typing import List


class Solution283:
    def moveZeroes(self, nums: List[int]):
        j = 0
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0
        print(nums)


s = Solution283()
s.moveZeroes([0, 2, 0, 1, 4])
# Expected output - 2, 1, 4, 0, 0
