class Suggestion:
    """
    Represents a single autocomplete suggestion.
    """
    def __init__(self, term, frequency=0, last_used=None, user_freq=None):
        self.term = term
        self.frequency = frequency
        self.last_used = last_used
        self.user_freq = user_freq or {}
        self.score = None

    def __repr__(self):
        return f"Suggestion(term={self.term}, score={self.score})"
