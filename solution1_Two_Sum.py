class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number_to_find = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == number_to_find:
                    return [i, j]


solution = Solution()
print(solution.twoSum([1, 3, 5, 7, 2], 9))
