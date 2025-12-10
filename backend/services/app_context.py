from engine.trie import TrieIndex
from engine.ranking import RankingEngine
from engine.typo_engine import TypoEngine
from engine.cache import SimpleCache
from engine.query_processor import QueryProcessor
from engine.user_logger import UserEventLogger
from utils.corpus_loader import load_corpus

class AppContext:
    trie = None
    typo_engine = None
    ranking = None
    cache = None
    query_processor = None
    logger = None

    @classmethod
    def initialize(cls):
        if cls.trie is None:
            print("Loading engine...")

            cls.trie = TrieIndex()
            corpus = load_corpus("data/initial_corpus.txt")
            for term, freq in corpus:
                cls.trie.insert(term, frequency=freq)

            cls.typo_engine = TypoEngine(cls.trie)
            cls.ranking = RankingEngine()
            cls.cache = SimpleCache()
            cls.logger = UserEventLogger(cls.trie)

            cls.query_processor = QueryProcessor(
                cls.trie, cls.typo_engine, cls.ranking, cls.cache
            )

            print("Engine loaded!")

        return cls.query_processor, cls.logger
