from typing import List


class Solution941:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        while (i < len(arr) and arr[i] > arr[i-1]):
            i += 1
        if(i == 1 or i == len(arr)):
            return False
        while (i < len(arr) and arr[i] < arr[i-1]):
            i += 1
        return i == len(arr)

s = Solution941()
answer = s.validMountainArray([0, 2, 3, 4, 5, 2, 1])
print(answer)
# Expected output: true
