def load_corpus(path):
    """
    Loads initial words for the Trie.
    Expect file with one term per line: "python"
    or "python,120" meaning frequency 120.
    """
    words = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            term = parts[0]
            freq = int(parts[1]) if len(parts) > 1 else 1
            words.append((term, freq))
    return words
