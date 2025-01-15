
'''
https://algo.monster/liteproblems/1244
'''

from sortedcontainers import SortedList # type: ignore
from collections import defaultdict
from random import choice

class Leaderboard:
    def __init__(self):

        self.scores_by_player = defaultdict(int)
        self.sorted_scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:

        if playerId not in self.scores_by_player:
            self.scores_by_player[playerId] = score
            self.sorted_scores.add(score)
        else:

            self.sorted_scores.remove(self.scores_by_player[playerId])
            self.scores_by_player[playerId] += score
            self.sorted_scores.add(self.scores_by_player[playerId])
        

    def top(self, K: int) -> int:
        return sum(self.sorted_scores[-K:])

    def reset(self, playerId: int) -> None:
        self.sorted_scores.remove(self.scores_by_player[playerId])
        del self.scores_by_player[playerId]
        
        
l = Leaderboard()

for _ in range(5):
    player_id = choice(range(1,4))
    score = choice(range(1,6))
    l.addScore(player_id, score)
    print("score added for player", player_id, " score: ", score)

print(l.scores_by_player)
print(l.top(2))

player_id = choice(range(1,4))
score = choice(range(1,6))
l.addScore(player_id, score)
print("score added for player", player_id, " score: ", score)

print(l.scores_by_player)
print(l.top(2))

l.reset(3)
print(l.scores_by_player)
print(l.top(2))

