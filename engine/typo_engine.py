from .models import Suggestion

def levenshtein_distance(a, b):
    """
    Classic dynamic programming Levenshtein distance.
    """
    dp = [[i + j if i == 0 or j == 0 else 0 for j in range(len(b) + 1)] 
          for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # delete
                dp[i][j - 1] + 1,      # insert
                dp[i - 1][j - 1] + cost  # replace
            )
    return dp[-1][-1]


class TypoEngine:
    """
    Finds fuzzy matches using edit distance.
    """

    def __init__(self, trie):
        self.trie = trie

    def find_fuzzy_candidates(self, query, max_distance=1):
        variants = set()

        # Generate strings with edit distance 1
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # Deletions
        for i in range(len(query)):
            variants.add(query[:i] + query[i+1:])

        # Insertions
        for i in range(len(query)+1):
            for ch in alphabet:
                variants.add(query[:i] + ch + query[i:])

        # Substitutions
        for i in range(len(query)):
            for ch in alphabet:
                variants.add(query[:i] + ch + query[i+1:])

        candidates = []
        for v in variants:
            node = self.trie.find_prefix_node(v)
            if node:
                candidates.extend(self.trie.collect_terms(node))

        # Remove duplicates
        unique = {c.term: c for c in candidates}
        return list(unique.values())
