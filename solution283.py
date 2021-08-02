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
