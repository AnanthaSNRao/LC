'''
https://algo.monster/liteproblems/253
'''

from typing import List
from itertools import accumulate

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_delta = [0] * 1000010

        for start, end in intervals:
            meeting_delta[start] += 1  
            meeting_delta[end] -= 1    

        return max(accumulate(meeting_delta))