# Autocomplete Engine (Full-Stack)

A full-stack autocomplete system with Python backend and an interactive Vue frontend.
The project demonstrates how modern autocomplete systems work internally — including tries, typo tolerance, ranking, personalization, caching, and debug visualization.


## Key Features
### Backend

- Trie-based prefix search
- Typo tolerance (edit distance)
- Advanced ranking:
  - Global frequency
  - User-specific frequency
  - Recency decay
  - Prefix boost

- User personalization
- In-memory caching
- User interaction logging
- Deep debug mode (internal pipeline visibility)
- REST API with FastAPI

### Frontend
- Live autocomplete search UI
- Clickable ranked suggestions
- Debug visualization of engine internals
- Trie tree rendering
- Ranking flow visualization
- Modular Vue components
- animated UI

## Project Structure
```bash
.
├── backend/
│   ├── engine/
│   │   ├── trie.py
│   │   ├── typo_engine.py
│   │   ├── ranking.py
│   │   ├── query_processor.py
│   │   ├── cache.py
│   │   ├── user_logger.py
│   │   └── models.py
│   │
│   ├── server/
│   │   ├── autocomplete.py
│   │   ├── app_context.py
│   │   └── models.py
│   │
│   ├── utils/
│   │   └── corpus_loader.py
│   │
│   ├── data/
│   │   └── initial_corpus.txt
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── components/
│   │   │   ├── SearchBar.vue
│   │   │   ├── SuggestionList.vue
│   │   │   ├── DebugPanel.vue
│   │   │   ├── PathSteps.vue
│   │   │   ├── RankFlow.vue
│   │   │   ├── TrieTree.vue
│   │   │   └── TrieNode.vue
│   │   ├── services/api.js
│   │   └── store/debugStore.js
│   │
│   └── package.json
│
└── README.md
```

## How Autocomplete Works?
Each query follows this pipeline:
1) Cache lookup (query + user)
2) Exact prefix search using Trie
3) Fuzzy search (only if no exact matches)
4) Candidate de-duplication
5) Prefix score boosting
6) Ranking (frequency, recency, personalization)
7) Caching results
8) Optional debug metadata generation


## Ranking Logic
Each suggestion’s final score is based on:
- Prefix boost for exact matches
- Global frequency (log-scaled)
- User frequency (higher weight)
- Recency decay (recent selections rank higher)

## Debug Mode

When debug mode is enabled, the backend returns:
- Prefix traversal path
- Exact vs fuzzy candidates
- Ranking input & output
- Trie subtree snapshot
- The frontend visualizes this using:
- PathSteps – prefix traversal
- RankFlow – scoring pipeline
- TrieTree / TrieNode – trie structure

This makes the engine fully transparent and explorable.

## Running the Backend
1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
2️⃣ Start the API server
```bash
uvicorn server.main:app --reload
```

Server runs at: http://localhost:8000

API base: http://localhost:8000/api


Running the Frontend
1️⃣ Install dependencies
```bash
npm install
```
2️⃣ Start dev server
```bash
npm run dev
```

Frontend runs at: http://localhost:5173 (or similar)

Expects backend running on localhost:8000
