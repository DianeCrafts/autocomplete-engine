from datetime import datetime

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.term = None
        self.frequency = 0
        self.last_used = None
        self.user_freq = {}

class TrieIndex:
    """
    Implements a Trie/PREFIX tree to store terms for fast lookup.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, term, frequency=1, timestamp=None, user_id=None):
        node = self.root
        for char in term:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True
        node.term = term
        node.frequency += frequency
        node.last_used = timestamp or datetime.now()
        if user_id:
            node.user_freq[user_id] = node.user_freq.get(user_id, 0) + 1

    def find_prefix_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def collect_terms(self, node, limit=None):
        results = []

        def dfs(n):
            if n.is_end:
                from .models import Suggestion
                results.append(Suggestion(n.term, n.frequency, n.last_used, n.user_freq))
            for child in n.children.values():
                dfs(child)

        dfs(node)
        return results[:limit] if limit else results