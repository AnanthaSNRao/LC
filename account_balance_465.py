'''
https://algo.monster/liteproblems/465
'''
from collections import defaultdict
from math import inf

class Solution:
    def min_transfers(self, transactions) -> int:
        balance = defaultdict(int)
        # Calculate the net balance for each person
        for from_person, to_person, amount in transactions:
            balance[from_person] -= amount
            balance[to_person] += amount
      
        # Filter out people with a zero balance as they do not need any transfers
        debts = [amount for amount in balance.values() if amount]
        number_of_people = len(debts)
      
        # Initialize the dp array to store minimum transfers for each subset
        # set fewest_transfers[i] = inf for all i, except fewest_transfers[0] = 0
        fewest_transfers = [inf] * (1 << number_of_people)
        fewest_transfers[0] = 0
      
        # Evaluate each subset of people
        for i in range(1, 1 << number_of_people):
            sum_of_debts = 0
            # Calculate the sum of debts for the current subset
            for j, debt in enumerate(debts):
                if i >> j & 1:
                    sum_of_debts += debt
          
            # If the sum of debts is zero, it's possible to settle within the group
            if sum_of_debts == 0:
                # The number of transactions needed is the bit count of i (number of set bits) minus 1
                fewest_transfers[i] = bin(i).count('1') - 1
              
                # Try to split the subset in different ways and keep the minimum transfers
                subset = (i - 1) & i
                while subset > 0:
                    fewest_transfers[i] = min(fewest_transfers[i], fewest_transfers[subset] + fewest_transfers[i ^ subset])
                    subset = (subset - 1) & i
      
        # The answer is in fewest_transfers[-1] which corresponds to the situation where all people are considered
        return fewest_transfers[-1]