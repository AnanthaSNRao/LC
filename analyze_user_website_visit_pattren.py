from collections import defaultdict, Counter
from typing import List

class Solution:
    def mostVisitedPattern(
        self, usernames: List[str], timestamps: List[int], websites: List[str]
    ) -> List[str]:
        # Create a dictionary to store the sites visited by each user
        users_visits = defaultdict(list)
        # Sort the data by timestamp and group websites by username
        for user, _, site in sorted(zip(usernames, timestamps, websites), key=lambda x: x[1]):
            users_visits[user].append(site)

        # Counter for tracking the frequency of each 3-sequence pattern
        patterns_count = Counter()

        # Iterate through each user's visited sites
        for sites in users_visits.values():
            number_of_sites = len(sites)
            unique_patterns = set()  # set to store unique 3-sequence patterns
            if number_of_sites > 2:  # Check if user has visited more than 2 sites
                # Generate all possible 3-sequence combinations
                for i in range(number_of_sites - 2):
                    for j in range(i + 1, number_of_sites - 1):
                        for k in range(j + 1, number_of_sites):
                            unique_patterns.add((sites[i], sites[j], sites[k]))
          
            # Update the count of each unique pattern
            for pattern in unique_patterns:
                patterns_count[pattern] += 1
      
        # Sort the patterns first by frequency (descending) and then lexicographically, and return the most common pattern
        return sorted(patterns_count.items(), key=lambda x: (-x[1], x[0]))[0][0]
