from engine.trie import TrieIndex
from engine.ranking import RankingEngine
from engine.typo_engine import TypoEngine
from engine.cache import SimpleCache
from engine.query_processor import QueryProcessor
from engine.user_logger import UserEventLogger
from utils.corpus_loader import load_corpus

def load_system():
    trie = TrieIndex()

    corpus = load_corpus("data/initial_corpus.txt")
    for term, freq in corpus:
        trie.insert(term, frequency=freq)

    typo_engine = TypoEngine(trie)
    ranking_engine = RankingEngine()
    cache = SimpleCache()
    logger = UserEventLogger(trie)

    qp = QueryProcessor(trie, typo_engine, ranking_engine, cache)
    return qp, logger

def main():
    qp, logger = load_system()

    print("\n--- Autocomplete Engine ---")
    user_id = "user_1"

    while True:
        prefix = input("\nEnter prefix: ")

        suggestions = qp.autocomplete(prefix, user_id=user_id)
        print("Suggestions:")
        for i, s in enumerate(suggestions):
            print(f"{i+1}. {s.term} (score={s.score:.3f})")

        choice = input("Pick one (enter number) or press ENTER to skip: ")
        if choice.isdigit():
            term = suggestions[int(choice)-1].term
            print(f"You selected: {term}")
            logger.log(user_id, term)

if __name__ == "__main__":
    main()
