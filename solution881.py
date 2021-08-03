from typing import List


class Solution881:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people)-1
        boat_number = 0

        while (left <= right):
            if(left == right):
                boat_number += 1
                break

            if(people[left]+people[right] <= limit):

                left += 1

            boat_number += 1
            right -= 1

        return boat_number


s = Solution881()
print(s.numRescueBoats([3, 2, 2, 1], 3))
#Output: 3
