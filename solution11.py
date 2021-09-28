"""
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


class Solution11:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxArea = 0
        while(l < r):
            maxArea = max(maxArea, min(height[l], height[r]) * (r-l))
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxArea


s = Solution11()
answer = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(answer)
