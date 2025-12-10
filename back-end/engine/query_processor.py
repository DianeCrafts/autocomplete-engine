class QueryProcessor:
    """
    Coordinates trie search, fuzzy search, ranking, and caching.
    """

    def __init__(self, trie, typo_engine, ranking_engine, cache):
        self.trie = trie
        self.typo_engine = typo_engine
        self.ranking = ranking_engine
        self.cache = cache

    def autocomplete(self, query, user_id=None, k=5, debug=False, disable_cache=False):
        debug_info = {
            "query": query,
            "prefix_path": [],
            "prefix_node": None,
            "exact_candidates": [],
            "fuzzy_candidates": [],
            "all_candidates": [],
            "candidate_terms": [],
            "rank_input": [],
            "rank_output": [],
            "trie_subtree": None,
        }

        # -----------------------------
        # 1. Cache lookup
        # -----------------------------
        if not disable_cache:
            cached = self.cache.get(query, user_id)
            if cached:
                return cached

        candidates = []

        # -----------------------------
        # 2. Exact prefix search
        # -----------------------------
        prefix_node, prefix_path = self.trie.find_prefix_node_with_path(query)
        debug_info["prefix_path"] = prefix_path

        exact_candidates = []
        if prefix_node:
            exact_candidates = self.trie.collect_terms(prefix_node)
        
        debug_info["exact_candidates"] = [c.term for c in exact_candidates]

        candidates.extend(exact_candidates)

        # -----------------------------
        # 3. Fuzzy search if needed
        # -----------------------------
        fuzzy_candidates = []
        if not exact_candidates:
            fuzzy_candidates = self.typo_engine.find_fuzzy_candidates(query)
            candidates.extend(fuzzy_candidates)

        debug_info["fuzzy_candidates"] = [c.term for c in fuzzy_candidates]

        # -----------------------------
        # 4. De-duplicate
        # -----------------------------
        unique = {c.term: c for c in candidates}.values()
        debug_info["candidate_terms"] = [c.term for c in unique]

        # -----------------------------
        # 5. Ranking
        # -----------------------------
        for c in unique:
            if c.term.startswith(query):   # exact match boost
                if c.score is None:
                    c.score = 0
                c.score += 10.0

        debug_info["rank_input"] = [
            {"term": c.term, "score": c.score} for c in unique
        ]

        ranked = self.ranking.rank(list(unique), user_id=user_id, limit=k)
        print(ranked)

        debug_info["rank_output"] = [
            {"term": c.term, "score": c.score} for c in ranked
        ]

        # -----------------------------
        # 6. Cache
        # -----------------------------
        self.cache.set(query, user_id, ranked)

        # -----------------------------
        # 7. Add Trie subtree for visualization
        # -----------------------------
        if prefix_node:
            debug_info["prefix_node"] = {
                "term": prefix_node.term,
                "is_end": prefix_node.is_end,
                "frequency": prefix_node.frequency,
                "children": list(prefix_node.children.keys())
            }
            debug_info["trie_subtree"] = self.trie.to_dict(prefix_node)

        # -----------------------------
        # Return debug version or normal version
        # -----------------------------
        if debug:
            return ranked, debug_info

        return ranked
