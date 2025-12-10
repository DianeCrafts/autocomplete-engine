class QueryProcessor:
    """
    Coordinates trie search, fuzzy search, ranking, and caching.
    """

    def __init__(self, trie, typo_engine, ranking_engine, cache):
        self.trie = trie
        self.typo_engine = typo_engine
        self.ranking = ranking_engine
        self.cache = cache

    def autocomplete(self, query, user_id=None, k=5):
        # -----------------------------
        # 1. Check Cache
        # -----------------------------
        cached = self.cache.get(query, user_id)
        if cached:
            return cached

        candidates = []

        # -----------------------------
        # 2. Exact prefix search
        # -----------------------------
        prefix_node = self.trie.find_prefix_node(query)

        exact_candidates = []
        if prefix_node:
            exact_candidates = self.trie.collect_terms(prefix_node)

        # Add them to main list
        candidates.extend(exact_candidates)

        # -----------------------------
        # 3. Only use fuzzy search if NO exact matches
        # -----------------------------
        if not exact_candidates:
            fuzzy_candidates = self.typo_engine.find_fuzzy_candidates(query)
            candidates.extend(fuzzy_candidates)

        # De-duplicate by term
        unique = {c.term: c for c in candidates}.values()

        # -----------------------------
        # 4. Ranking
        # Boost exact matches before ranking
        # -----------------------------
        for c in unique:
            if c.term.startswith(query):   # exact prefix match
                if c.score is None:
                    c.score = 0
                c.score += 10.0            # large boost → exact matches always dominate

        ranked = self.ranking.rank(list(unique), user_id=user_id, limit=k)

        # -----------------------------
        # 5. Cache results
        # -----------------------------
        self.cache.set(query, user_id, ranked)

        return ranked

