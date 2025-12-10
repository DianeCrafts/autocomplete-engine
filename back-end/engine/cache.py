class SimpleCache:
    """
    Basic dictionary-based cache.
    """

    def __init__(self):
        self.store = {}

    def get(self, prefix, user_id):
        return self.store.get((prefix, user_id), None)

    def set(self, prefix, user_id, suggestions):
        self.store[(prefix, user_id)] = suggestions
