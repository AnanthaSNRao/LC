from sortedcontainers import SortedList # type: ignore
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        # A mapping from player ID to their score
        self.scores_by_player = defaultdict(int)
        # A sorted list of scores for efficient ranking
        self.sorted_scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        """
        Add score to a player. If the player does not exist, create their record. 
        Otherwise, update their score and maintain the sorted order of scores.
        """
        if playerId not in self.scores_by_player:
            self.scores_by_player[playerId] = score
            self.sorted_scores.add(score)  # Player is new, add score directly
        else:
            # Player exists, remove the old score
            self.sorted_scores.remove(self.scores_by_player[playerId])
            # Update the player's score
            self.scores_by_player[playerId] += score
            # Add the updated score for the player
            self.sorted_scores.add(self.scores_by_player[playerId])

    def top(self, K: int) -> int:
        """
        Calculate the sum of the top K players' scores.
        """
        # Since the sorted_scores list is in ascending order, get the last K scores for top players
        return sum(self.sorted_scores[-K:])

    def reset(self, playerId: int) -> None:
        """
        Reset a player's score by removing it from the sorted list and player dictionary.
        """
        # Remove the player's score from the sorted list
        self.sorted_scores.remove(self.scores_by_player[playerId])
        # Remove the player's score from the dictionary
        del self.scores_by_player[playerId]
