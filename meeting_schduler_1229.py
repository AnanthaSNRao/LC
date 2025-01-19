'''
https://algo.monster/liteproblems/1229
'''

from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Sort the time slots for both people to allow for easy comparison
        slots1.sort()
        slots2.sort()
      
        # Initialize variables to track current index in slots1 and slots2
        index1 = index2 = 0
      
        # Get the total number of slots for both people
        total_slots1 = len(slots1)
        total_slots2 = len(slots2)
     
        # Iterate over the slots until at least one person's slots are fully checked
        while index1 < total_slots1 and index2 < total_slots2:
            # Find the overlapping start time of the current slots
            overlap_start = max(slots1[index1][0], slots2[index2][0])
            # Find the overlapping end time of the current slots
            overlap_end = min(slots1[index1][1], slots2[index2][1])
          
            # If the overlapping period is greater than or equal to the required duration
            if overlap_end - overlap_start >= duration:
                # Return the start time and start time plus the duration
                return [overlap_start, overlap_start + duration]
              
            # If the end time in slots1 is before the end time in slots2,
            # increase the index for slots1 to check the next slot
            if slots1[index1][1] < slots2[index2][1]:
                index1 += 1
            else:
                # Otherwise, increase the index for slots2 to check the next slot
                index2 += 1
              
        # If no overlapping period long enough for the meeting is found, return an empty list
        return []

# Example usage:
sol = Solution()
result = sol.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
print(result)