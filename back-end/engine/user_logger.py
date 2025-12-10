from datetime import datetime

class UserEventLogger:
    """
    Tracks user search behavior for frequency & recency.
    """

    def __init__(self, trie):
        self.trie = trie

    def log(self, user_id, term):
        self.trie.insert(term, frequency=1, timestamp=datetime.now(), user_id=user_id)
