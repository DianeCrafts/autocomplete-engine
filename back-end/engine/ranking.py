import math
from datetime import datetime

class RankingEngine:

    def score_item(self, s, user_id=None):
        score = 0

        # Base score (from QueryProcessor prefix boost)
        if s.score:
            score += s.score

        # Add global frequency (log scale so big numbers don't explode)
        score += math.log(1 + s.frequency)

        # Add user-specific frequency (bigger weight)
        if user_id and user_id in s.user_freq:
            score += 2 * s.user_freq[user_id]

        # Add recency boost
        if s.last_used:
            age_seconds = (datetime.now() - s.last_used).total_seconds()
            recency = 1 / (1 + age_seconds / 86400)  # decay per day
            score += recency

        return score

    def rank(self, items, user_id=None, limit=5):
        for s in items:
            s.score = self.score_item(s, user_id=user_id)

        # Sort by final score
        items.sort(key=lambda x: x.score, reverse=True)
        return items[:limit]
