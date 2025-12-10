import math
from datetime import datetime

class RankingEngine:
    """
    Computes scores for suggestions using frequency, recency, and personalization.
    """

    def __init__(self, alpha=1.0, beta=1.0, gamma=1.0):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def rank(self, candidates, user_id=None, now=None, limit=10):
        now = now or datetime.now()

        for s in candidates:
            freq_score = math.log(s.frequency + 1)

            if s.last_used:
                hours = (now - s.last_used).total_seconds() / 3600
                recency_score = 1 / (1 + hours)
            else:
                recency_score = 0

            personalization_score = s.user_freq.get(user_id, 0) if user_id else 0

            s.score = (
                self.alpha * freq_score +
                self.beta * recency_score +
                self.gamma * personalization_score
            )

        ranked = sorted(candidates, key=lambda x: x.score, reverse=True)
        return ranked[:limit]
